from django.test import TestCase
from django.contrib.auth import get_user_model

from jobs.models import PhotoJobHistory


class TestJobHistory(TestCase):

    def setUp(self):
        self.username = "hjh@aa.com"
        self.password = "1234"

        self.user = get_user_model().objects.create_user(
            username=self.username,
            password=self.password,
        )

        self.assertEqual(
            self.user.username,
            self.username,
        )

    def test_job_history_should_have_hash_id(self):

        photo_job_history = PhotoJobHistory.objects.create(
            user=self.user,
            theme=1,
            content="test",
        )

        self.assertTrue(photo_job_history.hash_id)
