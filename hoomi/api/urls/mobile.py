from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token

from api.views.mobile import *

urlpatterns = [
    url(r'^signup/$', UserCreateAPIView.as_view(), name="signup"),
    url(r'^login/$', obtain_jwt_token, name="login"),
]
