from rest_framework import serializers
from rest_framework.response import Response

from jobs.models import Occupation, Company


class CompanyModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = [
            "logo",
            "homepage",
            "name"
        ]


class OccupationModelSerializer(serializers.ModelSerializer):

    recomand = CompanyModelSerializer(source="company")

    class Meta:
        model = Occupation
        fields = [
            "recomand",
            "job_tags",
        ]
