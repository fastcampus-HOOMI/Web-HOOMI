from rest_framework.generics import ListAPIView

from api.serializers import SkillSerializer, DeveloperSerializer
from jobs.models import Skills


class SkillListAPIView(ListAPIView):
    serializer_class = SkillSerializer
    queryset = Skills.objects.all()


class UserSKillListAPIView(ListAPIView):
    serializer_class = DeveloperSerializer

    def get_queryset(self):
        user = self.request.user

        return user.developer_set.all()
