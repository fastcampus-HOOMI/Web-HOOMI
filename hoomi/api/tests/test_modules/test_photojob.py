from django.conf import settings
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase


class TestCreatePhotoJob(TestCase):

    def setUp(self):
        test_user = "test@test.com"
        test_password = "1234"
        test_last_name = "test"
        test_first_name = "API"

        signup_data = {
            "username": test_user,
            "password": test_password,
            "first_name": test_first_name,
            "last_name": test_last_name,
        }

        signup_response = self.client.post("/api/signup/", data=signup_data)

        self.assertEquals(
            201,
            signup_response.status_code,
        )

        login_data = {
            "username": test_user,
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

    def test_photo_job_create_not_image_should_return_400(self):
        test_theme = 1
        image = settings.PROJECT_ROOT_DIR + "/dist/media/test.png"

        data = {
            "theme": test_theme,
            "content_1": "1111",
        }

        response = self.client.post(
            "/api/job-history/",
            data=data,
            format="multipart",
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEquals(
            400,
            response.status_code,
        )

    def test_photo_job_create_should_return_201(self):
        test_theme = 1
        image = settings.PROJECT_ROOT_DIR + "/dist/media/test.png"

        test_image = SimpleUploadedFile(
            name="test.png",
            content=open(image, "rb").read(),
            content_type="image/png"
        )

        data = {
            "theme": test_theme,
            "image": test_image,
            "content": "1111",
        }

        response = self.client.post(
            "/api/job-history/",
            data=data,
            format="multipart",
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEquals(
            201,
            response.status_code,
        )
