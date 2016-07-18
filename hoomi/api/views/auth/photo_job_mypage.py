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
        photo_job = PhotoJobHistory.objects.filter(user=user)

        return PhotoJobHistory.objects.filter(user=user)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        if not queryset:
            user = request.user
            response_data = {
                "first_name": user.first_name,
                "last_name": user.last_name,
                "job": user.job.title,
                "username": user.username,
            }

            return Response(
                response_data,
                status.HTTP_200_OK,
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

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
