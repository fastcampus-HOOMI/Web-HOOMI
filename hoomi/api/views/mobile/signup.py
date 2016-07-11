from django.contrib.auth import get_user_model, authenticate

from rest_framework.generics import CreateAPIView
from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from api.serializers import UserSerializer


class MobileSignupAPIView(CreateAPIView):
    """
    Mobile 일반 회원가입
    """
    queryset = get_user_model()
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(
            username=username,
            password=password,
        )

        if user:
            response_data = {"Error": "Already Joiner"}

            return Response(
                response_data,
                status.HTTP_401_UNAUTHORIZED,
            )

        user = self.create(request, *args, **kwargs)
        response_data = {"Success": "Signup Success"}

        return Response(
            response_data,
            status.HTTP_201_CREATED,
        )
