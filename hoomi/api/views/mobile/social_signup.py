import random

from django.contrib.auth import get_user_model, authenticate

from rest_framework_jwt.settings import api_settings
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from api.serializers import UserSerializer

from social.apps.django_app.default.models import UserSocialAuth

from hashids import Hashids


class MobileOAuthSignupAPIView(APIView):
    """
    Mobile Social 회원가입(OAuth)
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        """
        해당 Provider가 존재하지 않으면 Response HTTP_406_NOT_ACCEPTABLE
        Access_token으로 기존회원이면 Response HTTP_401_UNAUTHORIZED

        User 생성 -> UserSocialAuth 생성
        """
        access_token = request.POST.get("access_token")
        provider = kwargs.get("provider")
        oauth_module_name = "users.oauth."

        try:
            provider_class = provider.title() + "OAuth"
            module = __import__(oauth_module_name+provider, fromlist=[provider_class])

            oauth = getattr(module, provider_class)()
            user_extra_data = oauth.signup(access_token)

            if 'error' in user_extra_data:
                response_data = {"Error": "Invalid Token Value"}

                return Response(
                    response_data,
                    status.HTTP_401_UNAUTHORIZED,
                )

        except ImportError:
            response_data = {"Error": "Not Supported Provider"}

            return Response(
                response_data,
                status.HTTP_406_NOT_ACCEPTABLE,
            )

        user = [
            data
            for data
            in UserSocialAuth.objects.all()
            if data.access_token == access_token
        ]

        if user:
            response_data = {"Error": "Already Joiner"}

            return Response(
                response_data,
                status.HTTP_401_UNAUTHORIZED,
            )

        hashids = Hashids(salt="iHA8aVD/", min_length=12)

        user = get_user_model().objects.create_user(
            email=user_extra_data.get("email"),
            password=hashids.encode(random.randint(1, 10000)),
            name=user_extra_data.get("name"),
        )

        social_user_data = {
            "access_token": access_token,
            "expires": "null",
            "id": extra_data.id,
        }

        social_user = UserSocialAuth.objects.create(
            provider=provider,
            uid=extra_data.id,
            extra_data=social_user_data,
            user_id=user.id,
        )

        response_data = {"Success": "Signup Success"}

        return Response(
            response_data,
            status.HTTP_201_CREATED,
        )
