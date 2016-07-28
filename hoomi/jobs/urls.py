from django.conf.urls import url

from jobs.views import *

urlpatterns = [
    url(r'^$', MainView.as_view(), name="main"),
    url(r'^select/$', SelectView.as_view(), name="select"),
    url(r'^resume/$', ResumeCreateView.as_view(), name="resume"),
    url(r'^mypage/$', ResumeMypageView.as_view(), name="myresume"),
    url(r'^recommend/$', Select.as_view(), name="recommend"),
]
