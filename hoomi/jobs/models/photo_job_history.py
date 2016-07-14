from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from .abstract_job_history import AbstractJobHistory


class PhotoJobHistory(AbstractJobHistory):

    hash_id = models.CharField(
        max_length=5,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user_theme
