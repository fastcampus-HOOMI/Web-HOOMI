from django.db import models


class Job(models.Model):
    title = models.CharField(
            max_length=120,
    )
