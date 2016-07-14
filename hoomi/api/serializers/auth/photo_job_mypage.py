from rest_framework import serializers

from jobs.models import PhotoJobHistory
from api.serializers.jobs import PhotoJobHistorySerializer, ExperienceSerializer


class PhotoJobUserMyPageSerializer(PhotoJobHistorySerializer):
    first_name = serializers.CharField(source="user.first_name")
    last_name = serializers.CharField(source="user.last_name")
    job = serializers.CharField(source="user.job.title")

    class Meta(PhotoJobHistorySerializer.Meta):
        model = PhotoJobHistory
        fields = [
            "first_name",
            "last_name",
            "job",
        ] + PhotoJobHistorySerializer.Meta.fields
