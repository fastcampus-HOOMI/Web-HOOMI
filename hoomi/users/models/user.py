from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from jobs.models import Job


class HoomiUserManager(UserManager):
    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except:
            return None


class User(AbstractUser):

    objects = HoomiUserManager()

    job = models.ForeignKey(
        Job,
        default=1,
    )

    def __str(self):
        return self.title
