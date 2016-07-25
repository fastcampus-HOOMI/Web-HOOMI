from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from jobs.models import Developer


class TestDeveloper(TestCase):

    def setUp(self):
        self.test_username = "test@test.com"
        self.password = "123456"
        first_name = "test"
        last_name = "developer"

        data = {
            "username": self.test_username,
            "password": self.password,
            "firstname": first_name,
            "lastname": last_name,
        }

        response = self.client.post(
            reverse("users:signup"),
            data=data,
        )

        self.assertEquals(
            302,
            response.status_code,
        )

        data = {
            "username": self.test_username,
            "password": self.password,
        }

        login = self.client.login(
            username=self.test_username,
            password=self.password
        )

        self.assertTrue(login)

        self.user = get_user_model().objects.get(
            username=self.test_username,
        )

        self.assertEqual(
            self.test_username,
            self.user.username,
        )

    def test_create_developer_should_return_201(self):
        self.test_skills = ["Java", "Python"]

        data = {
            "list[]": self.test_skills,
            "theme": 1,
        }

        response = self.client.post(
            reverse("jobs:select"),
            data=data,
        )

        self.assertEquals(
            302,
            response.status_code,
        )

        developer = self.user.developer_set.first()

        self.assertEqual(
            self.test_skills,
            developer.skills,
        )
