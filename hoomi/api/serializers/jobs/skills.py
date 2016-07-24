from rest_framework import serializers

from jobs.models import Skills


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["name", "wiki_url"]
