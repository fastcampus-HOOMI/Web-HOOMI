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

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class MobileOAuthSignupLoginAPIView(APIView):
    """
    Mobile Social 회원가입(OAuth)
    """
    serializer_class = UserSerializer
    permission_classes = (AllowAny, )
    authentication_classes = ()

    def post(self, request, *args, **kwargs):
        """
        해당 Provider가 존재하지 않으면 Response HTTP_406_NOT_ACCEPTABLE
        회원가입이 되어 있는데 Social User가 아니면 response HTTP_401_UNAUTHORIZED
        회원가입이 되어 있고 Social User이면 response JWT Token

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

        verify_user = get_user_model().objects.get_or_none(username=user_extra_data.get("email"))

        if verify_user:
            if verify_user.social_get_or_none(user=verify_user, user_id=verify_user.id):
                response_data = {"token": self.get_jwt_token(verify_user)}

                return Response(
                    response_data,
                    status.HTTP_201_CREATED,
                )

            response_data = {"Error": "Already Joiner"}

            return Response(
                response_data,
                status.HTTP_401_UNAUTHORIZED,
            )

        hashids = Hashids(salt="iHA8aVD/", min_length=12)

        user = get_user_model().objects.create_user(
            username=user_extra_data.get("email"),
            email=user_extra_data.get("email"),
            first_name=user_extra_data.get("first_name"),
            last_name=user_extra_data.get("last_name"),
            password=hashids.encode(random.randint(1, 10000)),
        )

        social_user_data = {
            "access_token": access_token,
            "expires": "null",
            "id": user_extra_data.get('id'),
        }

        social_user = UserSocialAuth.objects.create(
            provider=provider,
            uid=user_extra_data.get('id'),
            extra_data=social_user_data,
            user_id=user.id,
        )

        response_data = {"token": self.get_jwt_token(user)}

        return Response(
            response_data,
            status.HTTP_201_CREATED,
        )

    def get_jwt_token(self, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return token
