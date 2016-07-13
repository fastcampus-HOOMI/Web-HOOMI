from django.conf.urls import url
from jobs.views import *


urlpatterns = [
        url(r'^main/$', History.as_view(), name="history"),
        url(r'^select/$', Select.as_view(), name="select"),
]
