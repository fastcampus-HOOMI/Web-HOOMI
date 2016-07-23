from django.conf.urls import url
from jobs.views import *


urlpatterns = [
    url(r'^$', MainView.as_view(), name="main"),
    url(r'^select/$', SelectView.as_view(), name="select"),
]
