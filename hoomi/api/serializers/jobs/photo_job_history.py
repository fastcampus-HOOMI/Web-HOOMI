from rest_framework import serializers

from jobs.models import PhotoJobHistory
from jobs.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "image",
            "content",
        ]


class PhotoJobHistorySerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(source="experience_set", many=True)
    username = serializers.CharField(source="user.username")

    class Meta:
        model = PhotoJobHistory
        fields = [
            "username",
            "theme",
            "hash_id",
            "experiences",
        ]
