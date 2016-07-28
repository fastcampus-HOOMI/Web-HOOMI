from django.db import models


class Company(models.Model):
    name = models.CharField(
            max_length=120,
    )

    homepage = models.URLField(
    )

    logo = models.URLField(
    )

    def __str__(self):
        return self.name
