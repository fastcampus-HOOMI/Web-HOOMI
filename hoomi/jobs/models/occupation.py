from django.db import models
from django.contrib.postgres.fields import ArrayField


class Occupation(models.Model):

    job_experience = models.IntegerField(
        blank=True,
        null=True,
    )

    job_position = models.IntegerField(
            blank=True,
            null=True,
    )

    company = models.ForeignKey("company")

    job_tags = ArrayField(
            models.CharField(
                max_length=200,
                blank=True,
                null=True
            ))

    def __str__(self):
        return str(self.company)
