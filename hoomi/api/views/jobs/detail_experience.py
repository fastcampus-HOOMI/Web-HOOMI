from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from jobs.models import PhotoJobHistory
from api.paginations.detail import DetailPagination
from api.serializers import ExperienceSerializer


class ExperienceDetailListAPIView(ListAPIView):
    serializer_class = ExperienceSerializer
    pagination_class = DetailPagination
    lookup_field = "hash_id"

    def get_queryset(self):
        hash_id = self.kwargs.get("hash_id")
        photo = get_object_or_404(PhotoJobHistory, hash_id=hash_id)

        return photo.experience_set.all()
