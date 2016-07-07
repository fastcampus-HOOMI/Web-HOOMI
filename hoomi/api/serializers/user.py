from django.contrib.auth import get_user_model

from rest_framework import serializers
from jobs.models import Job


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    email = serializers.CharField(write_only=True)
    name = serializers.CharField(write_only=True)

    class Meta:
        model = get_user_model()

    def create(self, validated_data):

        user = get_user_model().objects.create_user(
            email=validated_data.get('email'),
            name=validated_data.get('name'),
            password=validated_data.get('password'),
        )

        return user
