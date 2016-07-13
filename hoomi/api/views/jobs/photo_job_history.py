from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from api.serializers.jobs import PhotoJobHistorySerializer

from jobs.models import PhotoJobHistory


class PhotoJobHistoryListAPIView(ListAPIView):
    serializer_class = PhotoJobHistorySerializer

    def get_queryset(self):
        photo_job_filter = PhotoJobHistory.objects.all()
        count = photo_job_filter.count()
        per = int(self.request.query_params.get("per", count))

        return photo_job_filter[:per]
