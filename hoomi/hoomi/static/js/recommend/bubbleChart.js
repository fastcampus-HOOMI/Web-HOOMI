(function() {

$(document).ready(function () {
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
      d3.json("{% url "api:skills:company" %}",function(error, language) {
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
});
