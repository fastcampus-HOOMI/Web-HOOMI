from django.conf.urls import url, include

from api.views.jobs import *

urlpatterns = [
    url(r'^$', PhotoJobHistoryListCreateAPIView.as_view(), name="photojob"),
    url(r'^(?P<hash_id>\w+)/$', ExperienceDetailListPatchDestroyAPIView.as_view(), name="detail"),
    url(r'^(?P<hash_id>\w+)/(?P<id>\d+)/$', ExperienecePatchDestoryAPIView.as_view(), name="detail"),
]
