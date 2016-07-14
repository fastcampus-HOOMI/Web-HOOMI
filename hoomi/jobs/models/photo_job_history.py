from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .abstract_job_history import AbstractJobHistory


class PhotoJobManager(models.Manager):
    def get_or_none(self, hash_id):
        try:
            return self.get(hash_id=hash_id)
        except ObjectDoesNotExist as exc:
            return None


class PhotoJobHistory(AbstractJobHistory):

    objects = PhotoJobManager()

    hash_id = models.CharField(
        max_length=5,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user_theme
