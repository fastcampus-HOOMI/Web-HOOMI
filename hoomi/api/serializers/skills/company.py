from rest_framework import serializers
from jobs.models import Skills


class SkillsModelSerializer(serializers.ModelSerializer):
    count = serializers.SerializerMethodField()
    text = serializers.CharField(source="name")

    class Meta:
        model = Skills
        fields = [
            "text",
            "count"
        ]

    def get_count(self, container):
        return container.get("count")
