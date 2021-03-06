from django.conf.urls import url
from django.http.response import HttpResponse
from users.views import *


urlpatterns = [
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^signup/$', SignupView.as_view(), name="signup"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
]
