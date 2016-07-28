from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from jobs.models import Occupation
from api.serializers import SkillsModelSerializer


class CompanySkillsAPIView(ListAPIView):

    serializer_class = SkillsModelSerializer

    def get_queryset(self):

        job_tags_set = Occupation.objects.values("job_tags")
        languages_count = {}
        for job_tags_dic in job_tags_set:
            job_tags = job_tags_dic["job_tags"]
            if job_tags:
                for job_tag in job_tags:
                    if job_tag is not "":
                        if job_tag in languages_count:
                            languages_count[job_tag] += 1
                        else:
                            languages_count[job_tag] = 1

        queryset = [{"name": key, "count": value} for key, value in languages_count.items() if value >= 15]

        return queryset
