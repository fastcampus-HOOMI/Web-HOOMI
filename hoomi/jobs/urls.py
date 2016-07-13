from django.conf.urls import url
from jobs.views import *


urlpatterns = [
        url(r'^main/$', CareerList.as_view(), name="careerlist"),
        url(r'^selectjob/$', SelectJob.as_view(), name="selectjob"),
]
