from django.conf.urls import url, include


urlpatterns = [
    url(r'^mobile/', include('api.urls.mobile', namespace="mobile")),
    url(r'^token/', include('api.urls.token', namespace="tokens")),
]
