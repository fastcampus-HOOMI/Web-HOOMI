from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('api.urls.auth', namespace="auth")),
    url(r'^token/', include('api.urls.token', namespace="tokens")),
    url(r'^job-history/', include('api.urls.job_history', namespace="job")),
]
