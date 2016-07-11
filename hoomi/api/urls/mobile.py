from django.conf.urls import url, include

from rest_framework_jwt.views import obtain_jwt_token

from api.views.mobile import *

urlpatterns = [
    url(r'^signup/$', MobileSignupAPIView.as_view(), name="signup"),
    url(r'^signup/(?P<provider>\w+)/$', MobileOAuthSignupAPIView.as_view(), name="login"),
    url(r'^login/$', MobileLoginAPIView.as_view(), name="login"),
    url(r'^login/(?P<provider>\w+)/$', MobileOAuthLoginAPIView.as_view(), name="login"),
]
