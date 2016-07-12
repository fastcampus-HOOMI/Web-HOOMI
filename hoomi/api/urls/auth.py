from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token

from api.views.auth import *

urlpatterns = [
    url(r'^signup/$', MobileSignupAPIView.as_view(), name="signup"),
    url(r'^oauth/(?P<provider>\w+)/$', MobileOAuthSignupLoginAPIView.as_view(), name="login"),
    url(r'^login/$', MobileLoginAPIView.as_view(), name="login"),
]
