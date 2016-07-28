(function() {
    $(document).ready(function() {
        var experienceCnt = 0, educationCnt = 0;
        
        $("#datepicker").datepicker({
            changeMonth: true, 
            changeYear: true,
            yearRange: '1950:2016',
            dayNames: ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일'],
            dayNamesMin: ['월', '화', '수', '목', '금', '토', '일'], 
            monthNamesShort: ['1','2','3','4','5','6','7','8','9','10','11','12'],
            monthNames: ['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월'],
            currentText: '오늘 날짜', 
            closeText: '닫기',
            dateFormat: "yy-mm-dd" 
        });
        

        $("#resume-form").validator().on("submit", function(e) {
            if (e.isDefaultPrevented()) {
                $.bootstrapGrowl("프로필을 채워주세요.", {
                  type: 'danger',
                  align: 'right',
                  delay: 1000,
                  allow_dismiss: true,
                  stackup_spacing: 10
                });
            } else {
                var experienceList = [], educationList = [];

                if(experienceCnt != 0 || educationCnt != 0) {
                    var experience = $('*[data-id="experience"]');
                    var education = $('*[data-id="education"]');

                    for(var i=0; i<experienceCnt; i++) {
                        var experienceObj = new Object();

                        var title = $($(experience).find('*[data-name="title"]')[i]).val()
                        var period = $($(experience).find('*[data-name="period"]')[i]).val()
                        var description = $($(experience).find('*[data-name="description"]')[i]).val()
                        
                        experienceObj["title"] = title;
                        experienceObj["period"] = period;
                        experienceObj["description"] = description;
                        
                        experienceList.push(experienceObj);
                    }
                    
                    for(var i=0; i<educationCnt; i++) {
                        var educationObj = new Object();

                        var title = $($(education).find('*[data-name="title"]')[i]).val()
                        var period = $($(education).find('*[data-name="period"]')[i]).val()
                        var description = $($(education).find('*[data-name="description"]')[i]).val()
                        
                        educationObj["title"] = title;
                        educationObj["period"] = period;
                        educationObj["description"] = description;
                        
                        educationList.push(educationObj);
                    }

                }

                var formList = $("#resume-form").serializeArray();
                formList.push({name: "experiences", value: JSON.stringify(experienceList)});
                formList.push({name: "educations", value: JSON.stringify(educationList)});
                
                $(this).ajaxSubmit({
                    type: "POST",
                    data: formList,
                    success: function(responseText, responseXML) {
                        $.bootstrapGrowl("저장되었습니다!", {
                          type: 'success',
                          align: 'right',
                          delay: 1000,
                          allow_dismiss: true,
                          stackup_spacing: 10
                        });
                        
                        setTimeout(function() {
                            window.location.replace("/mypage/");
                        }, 200);
                    },
                    error: function(error) {
                        debugger;
                    }
                });

                return false;
            }
        });

        $.ajax({
            type:"GET",
            url: "/api/skills/user/",
            success: function(data) {
                var skillListElement = $("#skill-list");
                var skillList = data[0].skills;

                for(var i=0; i<skillList.length; i++) {
                    var item = '<li class="list-group-item">' +
                                    '<span class="list-group-item-text">' +
                                        skillList[i] +
                                    '</span>' + 
                                '</li>';
                    
                    skillListElement.append(item);
                }
            },
            error: function(error) {
                $.bootstrapGrowl("현재 서버와의 통신에 문제가 있어 Skill를 못불러오고있습니다.", {
                  type: 'danger',
                  align: 'right',
                  delay: 1000,
                  allow_dismiss: true,
                  stackup_spacing: 10
                });
            }
        });

        $("#imageFile").on("change", function(event) {
            var reader = new FileReader();
            reader.onload = function(){
              var output = document.getElementById('profile-image');
              output.src = reader.result;
            };
            reader.readAsDataURL(event.target.files[0]); 
        });

        
        $(".timeline-panel").on("click", ".close", function() {
            if(confirm("정말 삭제하시겠습니까?")) {
                parentElement = $(this).parents(".work-experience");
                
                if( parentElement.data().id == "experience") {
                    experienceCnt -= 1;
                } else {
                    educationCnt -= 1;
                }

                $(this).parents(".work-experience")[0].remove();
            } else {
                return false;
            }
        });

        $(".caption-up a").click(function() {
            id = $(this)[0].id;
            var timelineElement, placeholderTitle, placeholderDescription, titlename, periodname, descriptionname, id;

            if( id == "add-experience") {
                experienceCnt += 1;

                timelineElement = $("#experience-timeline");
                placeholderTitle = "회사를 입력하세요";
                placeholderDescription = "회사에서 수행한 업무를 입력하세요";
                titlename = "experienceTitle_" + experienceCnt;
                periodname = "experiencePeriod_" + experienceCnt;
                id = "experience";
            } else {
                educationCnt += 1;

                timelineElement = $("#education-timeline");
                placeholderTitle = "학력을 입력하세요";
                placeholderDescription = "학력에 대한 정보를 입력하세요";
                titlename = "educationTitle_" + educationCnt;
                periodname = "educationPeriod_" + educationCnt;
                id = "education";
            }

            var addItem = '<div class="work-experience" data-id="' + id + '">' + 
                                        '<div class="col-md-11 col-sm-11">' +
                                            '<h3>' + 
                                                '<input type="text" class="form-control" data-name="title" placeholder="' + placeholderTitle + '">' +
                                            '</h3>' +
                                        '</div>' +
                                        '<div class="col-md-1 col-sm-1">' +
                                            '<button class="pull-right close">x</button>' + 
                                        '</div>' +
                                        '<div class="col-md-12 col-sm-12">' +
                                            '<small>' +
                                                '<div class="col-md-1 col-sm-2">' +
                                                    '<i class="fa fa-calendar"></i>' + 
                                                '</div>' +
                                                '<div class="col-md-11 col-sm-10">' +
                                                    '<input type="text" class="form-control" data-name="period" placeholder="기간을 입력하세요.(2014 - 2016)">' +
                                                '</div>' +
                                            '</small>' +
                                        '</div>' + 
                                        '<div class="col-md-12 col-sm-12">' +
                                            '<textarea class="form-control margin-top-05" cols="90" data-name="description" placeholder="' + placeholderDescription + '"></textarea>' +
                                        '</div>' +
                                    '</div>' +
                                '</div>';
           
            timelineElement.append(addItem);

        });
        
        if($("form").is("#mypage")) {
            debugger;
            alert("{{ user }}");
        }
        // if($('form').is('#mypage')){
        //     console.log({{ user}});
        //     alert("111");
        // }

    });
})();
