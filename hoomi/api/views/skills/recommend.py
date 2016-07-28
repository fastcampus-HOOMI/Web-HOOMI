from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from jobs.models import Occupation
from api.serializers import OccupationModelSerializer
from collections import OrderedDict


class RecommendAPIView(ListAPIView):

    serializer_class = OccupationModelSerializer
    lookup_field = "skill"

    def get_queryset(self):
        skill = self.kwargs.get("skill")

        occupation_by_skill = Occupation.objects.filter(
                job_tags__contains=[skill]
        )

        return occupation_by_skill

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        user_skill = ["Pyton", "Java"]
        topSix = []

        for query in queryset:
            lang_count = len(set(query.job_tags).intersection(user_skill))
            name = query.company.name
            logo = query.company.logo
            homepage = query.company.homepage
            if name not in topSix:
                topSix.append({
                    "name": name,
                    "count": lang_count,
                    "logo": logo,
                    "homepage": homepage,
                })
        newlist = sorted(topSix, key=lambda x: x['count'])
        return Response(newlist[:6])
