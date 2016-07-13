from django.contrib.auth.models import AbstractUser
from django.db import models

from jobs.models import Job


class User(AbstractUser):
    job = models.ForeignKey(
        Job,
        default=1,
    )

    def __str(self):
        return self.title
