import requests

from social.apps.django_app.default.models import UserSocialAuth

from .base import BaseOAuth


class FacebookOAuth(BaseOAuth):
    USER_DATA_URL = "https://graph.facebook.com/v2.3/me/"

    def signup(self, access_token):
        user_data = requests.get(
            self.USER_DATA_URL,
            params={
                "access_token": access_token,
                "fields": "email, name",
            }
        )

        return user_data.json()

    def login(self, user):
        social_user = UserSocialAuth.objects.get(user_id=user.id)
        access_token = social_user.extra_data.get("access_token")

        verify = requests.post(
            self.USER_DATA_URL,
            params={
                "access_token": access_token,
            }
        )

        return verify.json()
