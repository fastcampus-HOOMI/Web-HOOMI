from rest_framework import serializers

from jobs.models import PhotoJobHistory
from jobs.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "image",
            "content",
        ]


class PhotoJobHistorySerializer(serializers.ModelSerializer):
    experiences = ExperienceSerializer(source="experience_set", many=True)
    username = serializers.CharField(source="user.username", read_only=True)

    class Meta:
        model = PhotoJobHistory
        fields = [
            "username",
            "theme",
            "hash_id",
            "experiences",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        data = request.data
        image = request.FILES

        photo_job = PhotoJobHistory.objects.create(
            user=user,
            theme=data.get("theme"),
        )

        experience = Experience.objects.create(
            user=user,
            photo_job=photo_job,
            image=image.get("image"),
            content=data.get("content"),
        )

        return photo_job
