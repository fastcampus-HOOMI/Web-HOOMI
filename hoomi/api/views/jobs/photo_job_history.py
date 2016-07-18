from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from api.serializers.jobs import PhotoJobHistorySerializer

from api.paginations import StandardPagination
from jobs.models import PhotoJobHistory


class PhotoJobHistoryListAPIView(ListCreateAPIView):
    serializer_class = PhotoJobHistorySerializer
    pagination_class = StandardPagination

    def get_queryset(self):
        photo_job_filter = PhotoJobHistory.objects.all()
        count = photo_job_filter.count()
        per = int(self.request.query_params.get("per", count))

        return photo_job_filter[:per]

    def post(self, request, *args, **kwargs):
        if not request.FILES:
            response_data = {"Error": "At least one image required"}
            return Response(
                response_data,
                status.HTTP_400_BAD_REQUEST,
            )

        self.create(request, *args, **kwargs)

        response_data = {"Success": "Created data"}

        return Response(
            response_data,
            status.HTTP_201_CREATED,
        )
