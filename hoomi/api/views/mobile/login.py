from rest_framework.response import Response
from rest_framework import status

from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.views import JSONWebTokenAPIView, JSONWebTokenSerializer


jwt_response_payload_handler = api_settings.JWT_RESPONSE_PAYLOAD_HANDLER


class MobileLoginAPIView(JSONWebTokenAPIView):
    """
    Mobile 로그인
    """
    serializer_class = JSONWebTokenSerializer

    def post(self, request, *args, **kwargs):
        """
        일반 회원이면 JWT Token 발급
        소셜 회원이면 Facebook Authorization Server에 token 유효성 체크한 후 JWT Token 발급
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user')

            if 'provider' in kwargs:
                oauth_module_name = "users.oauth."

                try:
                    provider = kwargs.get("provider")
                    provider_class = provider.title() + "OAuth"
                    module = __import__(oauth_module_name+provider, fromlist=[provider_class])

                    oauth = getattr(module, provider_class)()
                    verify = oauth.login(user)

                    if 'error' in verify:
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

            jwt_token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(jwt_token, user, request)

            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {"Error": "Unable to login with provided credentials"}
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
