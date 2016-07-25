(function() {
    "use-strict";
    
    $(document).ready(function() {
        var languageList = [];
        var item = 
            '<div class="list-group-item skill-tag">' +
                '<h4 class="list-group-item-heading name"></h4>' +
            '</div>';
        var options = {
            valueNames: [
                "name",
                {data: ["id"]},
            ],
            searchClass: "skill-search",
            listClass: "skill-list",
            item: item,
            page: 5,
        };
        var skillList = new List("skill-list", options);

        $.ajax({
            type: "GET",
            url: "/api/skills/",
            success: function(data) {
                
                skillList.add(data);
            },
            error: function(data) {
                console.log(data);
            }
        });
 
        $(".tag-list").on("click", ".close", function() {
            var parentElement = $(this).parent("li")[0];
            var language = $(parentElement).find("span").html();
            var index = languageList.indexOf(language);

            languageList.splice(index, 1);

            $(this).parent("li")[0].remove();
        });
 
        $(".skill-list").on('click', ".skill-tag", function() {
            var ul = $(".tag-list");
            var language = $(this).find(".name").html();

            if(languageList.indexOf(language) != -1) {
                $.bootstrapGrowl("이미 고르신 Skill 입니다.", {
                  type: 'danger',
                  align: 'right',
                  delay: 1000,
                  allow_dismiss: true,
                  stackup_spacing: 10
                });
            } else {
                languageList.push(language); 
                element = 
                    '<li class="list-group-item">' +
                        '<span class="list-group-item-text">' + language + '</span>' +
                        '<button class="list-group-item-text pull-right close">x</button>' +
                    '</li>';

                ul.append(element);
                
                $(".skill-search").val("");
                skillList.search();
            } 
        });

        $("#skill-save").click(function() {
            if(languageList.length <= 0) {
                $.bootstrapGrowl("Skill을 하나 이상 골라주세요!", {
                  type: 'danger',
                  align: 'right',
                  delay: 1000,
                  allow_dismiss: true,
                  stackup_spacing: 10
                });
            } else {
                var data = {
                    "list": languageList
                };

                $.ajax({
                    type: "POST",
                    url: '/select/',
                    data: data,
                    success: function(data) { 
                        $.bootstrapGrowl("저장되었습니다!", {
                          type: 'success',
                          align: 'right',
                          delay: 1000,
                          allow_dismiss: true,
                          stackup_spacing: 10
                        });
                        
                        setTimeout(function() {
                            window.location.replace("/");
                        }, 200);
                    },
                    error: function(error) {
                        $.bootstrapGrowl("현재 서버와의 통신에 문제가 있습니다", {
                          type: 'danger',
                          align: 'right',
                          delay: 1000,
                          allow_dismiss: true,
                          stackup_spacing: 10
                        });
                    }
                });
            }
        });

    });
})();
