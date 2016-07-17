from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from api.serializers.auth import PhotoJobUserMyPageSerializer
from jobs.models import Job, PhotoJobHistory


class PhotoJobMyPageListAPIView(ListAPIView):
    serializer_class = PhotoJobUserMyPageSerializer

    def get_queryset(self):
        user = self.request.user
        return PhotoJobHistory.objects.filter(user=user)

    def patch(self, request, *args, **kwargs):
        job_id = request.data.get('job')
        job_title = get_object_or_404(Job, id=job_id)

        user = request.user
        user.job.title = job_title.title
        user.save()

        response_data = {
            "username": user.username,
            "job": user.job.title,
        }

        return Response(
            response_data,
            status.HTTP_200_OK,
        )
