from rest_framework import serializers

from django.shortcuts import get_object_or_404

from jobs.models import PhotoJobHistory
from jobs.models import Experience


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = [
            "id",
            "image",
            "content",
            "page",
        ]

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        hash_id = request.parser_context.get("kwargs").get("hash_id")

        photo_job = get_object_or_404(
            user.photojobhistory_set,
            hash_id=hash_id,
        )

        # user -> Image Field save required
        # photo_job -> Experience create ForeignKey required
        validated_data["user"] = user
        validated_data["photo_job"] = photo_job

        ModelClass = self.Meta.model

        try:
            instance = ModelClass.objects.create(**validated_data)
        except TypeError as exc:
            msg = (
                'Got a `TypeError` when calling `%s.objects.create()`. '
                'This may be because you have a writable field on the '
                'serializer class that is not a valid argument to '
                '`%s.objects.create()`. You may need to make the field '
                'read-only, or override the %s.create() method to handle '
                'this correctly.\nOriginal exception text was: %s.' %
                (
                    ModelClass.__name__,
                    ModelClass.__name__,
                    self.__class__.__name__,
                    exc
                )
            )
            raise TypeError(msg)

        return instance


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

        photo_job = PhotoJobHistory.objects.create(
            user=user,
            theme=data.get("theme"),
        )

        return photo_job
