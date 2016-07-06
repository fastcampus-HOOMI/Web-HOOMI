from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from jobs.models import Job


class User(AbstractBaseUser):
    job = models.ForeignKey(Job)
    name = models.CharField(
            max_length=60,
    )
    email = models.EmailField(
            unique=True,
    )
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email
