from django.db import models


class Skills(models.Model):
    name = models.TextField()
    wiki_url = models.URLField()

    def __str__(self):
        return self.name
