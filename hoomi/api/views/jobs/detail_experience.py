from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import status

from jobs.models import PhotoJobHistory
from api.paginations.detail import DetailPagination
from api.serializers import ExperienceSerializer


class ExperienceDetailListPatchDestroyAPIView(mixins.ListModelMixin,
                                              mixins.CreateModelMixin,
                                              GenericAPIView):

    serializer_class = ExperienceSerializer
    pagination_class = DetailPagination
    lookup_field = "hash_id"

    def get_queryset(self):
        hash_id = self.kwargs.get("hash_id")
        photo_job = get_object_or_404(
            PhotoJobHistory,
            hash_id=hash_id,
        )

        return photo_job.experience_set.all().order_by("page")

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_photo_job(self):
        user = self.request.user
        hash_id = self.kwargs.get("hash_id")
        photo_job = get_object_or_404(
            user.photojobhistory_set,
            hash_id=hash_id,
        )

        return photo_job

    def post(self, request, *args, **kwargs):
        page = request.data.get("page")
        duplicate_page = self.get_photo_job().experience_set.filter(page=page)

        if not request.FILES or duplicate_page:
            msg = "duplicate page" if duplicate_page else "image required"

            response_data = {"Error": msg}
            return Response(
                response_data,
                status.HTTP_400_BAD_REQUEST,
            )

        return self.create(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        photo_job = self.get_photo_job()

        filter_key = {
            key: value
            for key, value
            in request.data.items()
            if key == "theme"
        }

        if filter_key:
            photo_job.theme = filter_key.get("theme")
            photo_job.save()

        response_data = {
            "username": photo_job.user.username,
            "theme": photo_job.theme,
        }

        return Response(
            response_data,
            status.HTTP_200_OK,
        )

    def delete(self, request, *args, **kwargs):
        photo_job = self.get_photo_job()

        photo_job.delete()

        return Response(
            {},
            status.HTTP_204_NO_CONTENT
        )
