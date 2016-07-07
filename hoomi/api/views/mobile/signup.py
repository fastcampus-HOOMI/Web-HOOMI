from django.contrib.auth import get_user_model

from rest_framework.generics import CreateAPIView
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from api.serializers import UserSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()
