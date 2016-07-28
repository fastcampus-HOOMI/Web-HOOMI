(function() {
    $(document).ready(function() { 
        function appendRecommend(lang){	
            $.ajax({
              url: "/api/skills/recommend/" + lang + "/",
              type: "GET",
              success: function(data){
                var getlength = data.length;
                
                $("#secondrow").replaceWith('<div class="row" id="secondrow"></div>');
                //recommandCompanyElement.replaceWith('<div class="row" id="secondrow"></div>');
                data.forEach(function(jobs){
                    
                    var imgUrl = jobs.logo;
                    var recommendPoint = "Point : " + jobs.count;
                    var homePage = jobs.homepage; 
                var recommendation = 
                    '<div class="col-xs-6 col-md-2"><div class="thumbnail hovereffect">' + 
                        '<img class="img-responsive" src="' + imgUrl + '" alt="">' + 
                        '<div class="overlay">' + 
                            '<h2>' + recommendPoint + '</h2>' + 
                            '<a class="info" target="_blank" href="' + homePage + '">지원하러 가기</a>' +
                        '</div>' + 
                    '</div>' + 
                '</div>';
                $("#secondrow").append(recommendation);
             }) }, 
              error: function(error){
                console.log(error);
              }
            });
        }
        
        
        var margin = {top: 20, right: 20, bottom: 30, left: 40},
            width = 500 - margin.left - margin.right,
            height =300  - margin.top - margin.bottom;
        var x = d3.scale.ordinal()
            .rangeRoundBands([0, width], .1);

        var y = d3.scale.linear()
            .range([height, 0]);

        var xAxis = d3.svg.axis()
            .scale(x)
            .orient("bottom");

        var yAxis = d3.svg.axis()
            .scale(y)
            .orient("left")
            .ticks(10, "회");

        var svg = d3.select(".barChart").append("svg")
            .attr("width", width + margin.left + margin.right)
            .attr("height", height + margin.top + margin.bottom)
          .append("g")
            .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

        svg.append("g")
            .attr("class", "x axis")
            .attr("transform", "translate(0," + height + ")")
            
        svg.append("g")
            .attr("class", "y axis")
          .append("text") // just for the title (ticks are automatic)
            .attr("transform", "rotate(-90)") // rotate the text!
            .attr("y", 6)
            .attr("dy", ".71em")
            .style("text-anchor", "end")
            .text("count");

        console.log("1111");
        function type(d) {
          // + coerces to a Number from a String (or anything)
          d.count = +d.count;
          return d;
        }

        console.log("22222");
        d3.json("/api/skills/company/", function(error, data) {
          replay(data);
        });
        function replay(data) {
          var slices = [];
          for (var i = 0; i < data.length; i++) {
            slices.push(data.slice(0, i+1));
          }
          slices.forEach(function(slice, index){
            setTimeout(function(){
              draw(slice);
            }, index * 300);
          });
        }

        function draw(data) {
          // measure the domain (for x, unique letters) (for y [0,maxFrequency])
          // now the scales are finished and usable
          x.domain(data.map(function(d) { return d.text; }));
          y.domain([0, d3.max(data, function(d) { return d.count; })]);

          // another g element, this time to move the origin to the bottom of the svg element
          // someSelection.call(thing) is roughly equivalent to thing(someSelection[i])
          //   for everything in the selection\
          // the end result is g populated with text and lines!
          svg.select('.x.axis').transition().duration(300).call(xAxis);

          // same for yAxis but with more transform and a title
          svg.select(".y.axis")
              .transition().duration(300).call(yAxis)

          // THIS IS THE ACTUAL WORK!
              var bars = svg.selectAll(".bar").data(data, function(d) { return d.text; })      // (data) is an array/iterable thing, second argument is an ID generator function

          bars.exit()
            .transition()
              .duration(300)
            .attr("y", y(0))
            .attr("height", height - y(0))
            .style('fill-opacity', 1e-6)
            .remove();


          // data that needs DOM = enter() (a set/selection, not an event!)
          bars.enter()    
            .append("rect")
            .attr("class", "bar").on('click', function(){
            appendRecommend(data[data.length-1].text);})
            .attr("y", y(0))
            .attr("height", height - y(0));

          // the "UPDATE" set:
          bars.transition()
            .duration(300).attr("x", function(d) { return x(d.text); }) // (d) is one item from the data array, x is the scale object from above
            .attr("width", x.rangeBand()) // constant, so no callback function(d) here
            .attr("y", function(d) { return y(d.count); })
            .attr("height", function(d) { return height - y(d.count); }); // flip the height, because y's domain is bottom up, but SVG renders top down
        }

        $.extend(d3.svg.BubbleChart.prototype, {
            registerClickEvent: function (node) {
                  var self = this;
                  var swapped = false;
                  node.style("cursor", "pointer").on("click", function (d) {
                    self.clickedNode = d3.select(this);
                    // custom
                    self.getCompany(d);
                    self.event.send("click", self.clickedNode);
                    self.reset(self.centralNode);
                    self.moveToCentral(self.clickedNode);
                    self.moveToReflection(self.svg.selectAll(".node:not(.active)"), swapped);
                    swapped = !swapped;
                  });  
                },
            getCompany: function(d) {
                appendRecommend(d.item.text);
            }
        });
        
        d3.json("/api/skills/developer/",function(error, language) {
        var bubbleChart = new d3.svg.BubbleChart({
            supportResponsive: true,
            //container: => use @default
            size: 600,
            //viewBoxSize: => use @default
            innerRadius: 600 / 3.5,
            //outerRadius: => use @default
            radiusMin: 50,
            //radiusMax: use @default
            //intersectDelta: use @default
            //intersectInc: use @default
            //circleColor: use @default
            data:{
              items: language,
              eval: function (item) {return item.count;},
              classed: function (item) {return item.text.split(" ").join("");}
            },
            plugins: [
              {
                name: "central-click",
                options: {
                  text: "(See more detail)",
                  style: {
                    "font-size": "12px",
                    "font-style": "italic",
                    "font-family": "Source Sans Pro, sans-serif",
                    //"font-weight": "700",
                    "text-anchor": "middle",
                    "fill": "white"
                  },
                  attr: {dy: "65px"},
                  centralClick: function() {
                    alert("Here is more details!!");
                  }
                }
              },
              {
                name: "lines",
                options: {
                  format: [
                    {// Line #0
                      textField: "count",
                      classed: {count: true},
                      style: {
                        "font-size": "28px",
                        "font-family": "Source Sans Pro, sans-serif",
                        "text-anchor": "middle",
                        fill: "white"
                      },
                      attr: {
                        dy: "0px",
                        x: function (d) {return d.cx;},
                        y: function (d) {return d.cy;}
                      }
                    },
                    {// Line #1
                      textField: "text",
                      classed: {text: true},
                      style: {
                        "font-size": "14px",
                        "font-family": "Source Sans Pro, sans-serif",
                        "text-anchor": "middle",
                        fill: "white"
                      },
                      attr: {
                        dy: "20px",
                        x: function (d) {return d.cx;},
                        y: function (d) {return d.cy;}
                      }
                    }
                  ],
                  centralFormat: [
                    {// Line #0
                      style: {"font-size": "50px"},
                      attr: {}
                    },
                    {// Line #1
                      style: {"font-size": "30px"},
                      attr: {dy: "40px"}
                    }
                  ]
                }
              }]
          });
    });

  });
})();
