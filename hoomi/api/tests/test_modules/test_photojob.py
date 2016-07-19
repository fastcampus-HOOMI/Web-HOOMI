import json

from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.conf import settings


class TestCreatePhotoJob(TestCase):

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

        signup_response = self.client.post("/api/signup/", data=signup_data)

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

        test_content = "test_job_create"

        data = {
            "theme": test_theme,
            "image": test_image,
            "content": test_content,
        }

        response = self.client.post(
            "/api/job-history/",
            data=data,
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEquals(
            201,
            response.status_code,
        )

        self.assertEqual(
            test_content,
            response.status_code,
        )

    def get_photo_job(self):
        self.test_photo_job_create_should_return_201()

        user = get_user_model().objects.get(username=self.test_user)
        photo_job = user.photojobhistory_set.first()

        return photo_job

    def test_photo_job_get_list_should_return_200(self):
        photo_job = self.get_photo_job()

        hash_id = photo_job.hash_id

        set_uri = "/api/job-history/" + hash_id + "/"

        response = self.client.get(
            set_uri,
            data={},
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEquals(
            200,
            response.status_code,
        )

    def test_photo_job_patch_shoud_return_200(self):
        photo_job = self.get_photo_job()
        test_theme = 22

        set_uri = "/api/job-history/{hash_id}/".format(
            hash_id=photo_job.hash_id,
        )

        data = {
            "test_key": "111",
            "theme": test_theme,
        }

        response = self.client.patch(
            path=set_uri,
            data=json.dumps(data),
            content_type="application/json",
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEqual(
            200,
            response.status_code,
        )

        self.assertEqual(
            test_theme,
            response.data.get("theme"),
        )

        # Validation another key
        self.assertEqual(
            False,
            response.data.get("test_key", False)
        )

    def test_photo_job_delete_should_return_204(self):
        photo_job = self.get_photo_job()

        set_uri = "/api/job-history/{hash_id}/".format(
            hash_id=photo_job.hash_id,
        )

        response = self.client.delete(
            path=set_uri,
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEqual(
            204,
            response.status_code,
        )

    def test_experience_create_should_return_201(self):
        photo_job = self.get_photo_job()

        set_uri = "/api/job-history/{hash_id}/".format(
            hash_id=photo_job.hash_id,
        )

        image = settings.PROJECT_ROOT_DIR + "/dist/media/test.png"
        test_content = "test_create"

        test_image = SimpleUploadedFile(
            name="test.png",
            content=open(image, "rb").read(),
            content_type="image/png"
        )

        data = {
            "image": test_image,
            "content": test_content,
        }

        response = self.client.post(
            path=set_uri,
            data=data,
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEqual(
            201,
            response.status_code,
        )

        self.assertEqual(
            test_content,
            response.data.get("content"),
        )

    def test_experience_patch_shoud_return_200(self):
        photo_job = self.get_photo_job()

        set_uri = "/api/job-history/{hash_id}/{id}/".format(
            hash_id=photo_job.hash_id,
            id=photo_job.experience_set.first().id,
        )

        test_content = "test_create"

        data = {
            "content": test_content,
        }

        response = self.client.patch(
            path=set_uri,
            data=json.dumps(data),
            content_type="application/json",
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEqual(
            200,
            response.status_code,
        )

        self.assertEqual(
            test_content,
            response.data.get("content"),
        )

    def test_experience_delete_should_return_204(self):
        photo_job = self.get_photo_job()

        hash_id = photo_job.hash_id
        set_uri = "/api/job-history/{hash_id}/{id}/".format(
            hash_id=photo_job.hash_id,
            id=photo_job.experience_set.first().id,
        )

        response = self.client.delete(
            path=set_uri,
            HTTP_AUTHORIZATION="JWT {token}".format(
                token=self.token,
            )
        )

        self.assertEqual(
            204,
            response.status_code,
        )
