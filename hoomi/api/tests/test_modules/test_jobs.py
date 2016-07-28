from django.core.urlresolvers import reverse
from django.test import TestCase


class TestJobs(TestCase):

    def setUp(self):
        self.test_user = "test@test.com"
        test_password = "1234"
        test_last_name = "test"
        test_first_name = "API"

        signup_data = {
            "username": self.test_user,
            "password": test_password,
            "first_name": test_first_name,
            "last_name": test_last_name,
        }

        signup_response = self.client.post(
            "/api/signup/",
            data=signup_data
        )

        self.assertEquals(
            201,
            signup_response.status_code,
        )

        login_data = {
            "username": self.test_user,
            "password": test_password,
        }

        login_response = self.client.post(
            "/api/login/",
            data=login_data,
        )

        self.assertEquals(
            200,
            login_response.status_code,
        )

        self.token = login_response.data.get("token")

        self.assertTrue(self.token)

    def test_skills_all_should_return_201(self):
        response = self.client.get(
            "/api/skills/",
            data={},
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEquals(
            200,
            response.status_code,
        )

    def test_user_skills_should_return_200(self):
        response = self.client.get(
            "/api/skills/user/",
            data={},
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEquals(
            200,
            response.status_code,
        )
