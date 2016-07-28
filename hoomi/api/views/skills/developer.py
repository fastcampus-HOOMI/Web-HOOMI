from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from jobs.models import Developer, Occupation


class DeveloperAPIView(APIView):

    def get(self, request, *args, **kwargs):
        current_user = self.request.user
        developer = current_user.developer_set.first()
        lang_with_count = []
        for select_lang in developer.skills:
            count = len(Occupation.objects.filter(job_tags__contains=[select_lang]))
            text = select_lang
            lang_with_count.append({
                "text": text,
                "count": count,
            })

        return Response(
            lang_with_count,
            status.HTTP_200_OK,
        )
