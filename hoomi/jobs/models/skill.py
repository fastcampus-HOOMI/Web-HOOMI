from django.db import models


class Skill(models.Model):

    name = models.CharField(
            max_length=100,
            blank=True,
            null=True,
            )
    count = models.IntegerField(
            blank=True,
            null=True,
            )

    def __str__(self):
        return self.name
