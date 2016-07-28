from rest_framework import serializers

from jobs.models import Skills, Developer


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["id", "name", "wiki_url"]


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = ["skills"]
