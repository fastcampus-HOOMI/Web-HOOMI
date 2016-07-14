from rest_framework import serializers

from jobs.models import PhotoJobHistory
from jobs.models import Experience


class ExperienceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "image",
            "content",
        ]


class PhotoJobHistorySerializer(serializers.HyperlinkedModelSerializer):
    experiences = ExperienceSerializer(source="experience_set", many=True)

    class Meta:
        model = PhotoJobHistory
        fields = [
            "theme",
            "hash_id",
            "experiences",
        ]
