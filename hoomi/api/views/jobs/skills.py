from rest_framework.generics import ListAPIView

from api.serializers import SkillSerializer
from jobs.models import Skills


class SkillListAPIView(ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skills.objects.all()
