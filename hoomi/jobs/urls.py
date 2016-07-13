from django.conf.urls import url
from jobs.views import *


urlpatterns = [
        url(r'^main/$', JobHistory.as_view(), name="job_history"),
        url(r'^selectjob/$', SelectJob.as_view(), name="select_job"),
]
