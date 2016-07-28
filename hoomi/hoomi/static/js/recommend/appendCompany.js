(function() {
    $(document).ready(function() {
        function appendRecommend(lang){	$.ajax({
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
    
    });
});
