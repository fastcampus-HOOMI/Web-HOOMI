from django.db import models


class Job(models.Model):
    title = models.CharField(
            max_length=120,
            default=1,
    )

    def __str__(self):
        return self.title
