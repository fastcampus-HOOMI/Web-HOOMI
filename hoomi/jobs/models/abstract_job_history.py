from django.db import models

from django.conf import settings


class AbstractJobHistory(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    theme = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @property
    def user_theme(self):
        return "{user} - {theme}".format(
            user=self.user,
            theme=self.theme,
        )
