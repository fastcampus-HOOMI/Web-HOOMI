from rest_framework.generics import ListAPIView

from api.serializers.auth import PhotoJobUserMyPageSerializer
from jobs.models import PhotoJobHistory


class PhotoJobMyPageListAPIView(ListAPIView):
    serializer_class = PhotoJobUserMyPageSerializer

    def get_queryset(self):
        user = self.request.user
        return PhotoJobHistory.objects.filter(user=user)
