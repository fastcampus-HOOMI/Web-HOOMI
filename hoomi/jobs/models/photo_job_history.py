
from django.db import models

from .abstract_job_history import AbstractJobHistory


class PhotoJobHistory(AbstractJobHistory):

    hash_id = models.CharField(
        max_length=5,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.user_theme
