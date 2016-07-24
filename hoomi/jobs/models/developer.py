from django.contrib.postgres.fields import ArrayField
from django.db import models

from .abstract_job_history import AbstractJobHistory


class Developer(AbstractJobHistory):
    skills = ArrayField(models.CharField(
        max_length=30,
    ))
    interest_company = ArrayField(models.CharField(
        max_length=100,
    ))

    def __str__(self):
        return self.user
