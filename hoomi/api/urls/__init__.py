from django.conf.urls import url, include

from api.views.jobs import SkillListAPIView


urlpatterns = [
    url(r'^', include('api.urls.auth', namespace="auth")),
    url(r'^token/', include('api.urls.token', namespace="tokens")),
    url(r'^job-history/', include('api.urls.jobs', namespace="jobs")),
    url(r'^skills/', SkillListAPIView.as_view()),
]
