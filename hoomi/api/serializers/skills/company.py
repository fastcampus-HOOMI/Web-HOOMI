from rest_framework import serializers
from jobs.models import Skill


class SkillsModelSerializer(serializers.ModelSerializer):

    text = serializers.CharField(source="name")

    class Meta:
        model = Skill
        fields = [
                "text",
                "count",
                ]
