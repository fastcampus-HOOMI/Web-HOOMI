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
        """
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            user = serializer.object.get('user')

            jwt_token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(jwt_token, user, request)

            return Response(response_data, status=status.HTTP_201_CREATED)

        response_data = {"Error": "Unable to login with provided credentials"}
        return Response(response_data, status=status.HTTP_401_UNAUTHORIZED)
