from django.conf.urls import url

from api.views.jobs import *


urlpatterns = [
    url(r'^$', SkillListAPIView.as_view(), name="all"),
    url(r'^user/$', UserSKillListAPIView.as_view(), name="user"),
]
