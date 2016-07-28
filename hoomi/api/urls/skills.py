from django.conf.urls import url

from api.views.skills import *
from api.views.jobs import *


urlpatterns = [
    url(r'^$', SkillListAPIView.as_view(), name="all"),
    url(r'^user/$', UserSKillListAPIView.as_view(), name="user"),
    url(r'^company/$', CompanySkillsAPIView.as_view(), name="company"),
    url(r'^recommend/(?P<skill>\w+)/$', RecommendAPIView.as_view(), name="recommend"),
]
