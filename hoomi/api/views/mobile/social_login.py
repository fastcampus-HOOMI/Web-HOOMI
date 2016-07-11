from django.contrib.auth import get_user_model

from rest_framework.response import Response
from rest_framework import status

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView, JSONWebTokenSerializer

from social.apps.django_app.default.models import UserSocialAuth

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class MobileOAuthLoginAPIView(JSONWebTokenAPIView):
    """
    Mobile 로그인
    """
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        소셜 회원 이면 Post Token Validation Check
        저장된 Token이랑 Post Token Check
        """
        if 'provider' in kwargs:

            oauth_module_name = "users.oauth."

            try:
                provider = kwargs.get("provider")
                provider_class = provider.title() + "OAuth"
                module = __import__(oauth_module_name+provider, fromlist=[provider_class])

                oauth = getattr(module, provider_class)()
                access_token = self.request.POST.get("access_token")

                verify = oauth.login(access_token)

                if 'error' in verify:
                    response_data = {"Error": "Invalid Token Value"}

                    return Response(
                        response_data,
                        status.HTTP_401_UNAUTHORIZED,
                    )

                social_user = [
                    data
                    for data
                    in UserSocialAuth.objects.all()
                    if data.access_token == access_token
                ]

                if social_user:
                    user = get_user_model().objects.get(pk=social_user[0].user_id)

                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)

                    response_data = {"token": token}

                    return Response(response_data, status=status.HTTP_201_CREATED)

            except ImportError:
                response_data = {"Error": "Not Supported Provider"}

                return Response(
                    response_data,
                    status.HTTP_406_NOT_ACCEPTABLE,
                )

        response_data = {"Error": "Unable to login with provided credentials"}
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
