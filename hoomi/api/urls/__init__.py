from django.conf.urls import url, include

urlpatterns = [
    url(r'^token/', include('api.urls.token', namespace="tokens")),
]
