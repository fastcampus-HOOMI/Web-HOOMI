from rest_framework.generics import GenericAPIView
from rest_framework import mixins

from django.shortcuts import get_object_or_404

from jobs.models import Experience
from api.serializers import ExperienceSerializer


class ExperienecePatchDestoryAPIView(mixins.UpdateModelMixin,
                                     mixins.DestroyModelMixin,
                                     GenericAPIView):

    serializer_class = ExperienceSerializer
    lookup_field = "id"

    def get_queryset(self):
        user = self.request.user
        hash_id = self.kwargs.get("hash_id")
        id = self.kwargs.get("id")

        photo_job = get_object_or_404(
            user.photojobhistory_set,
            hash_id=hash_id
        )

        return photo_job.experience_set.all()

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
