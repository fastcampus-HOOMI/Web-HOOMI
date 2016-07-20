import datetime
import os

from django.db import models
from django.conf import settings


def set_filename_format(now, instance, filename):
    """
    file format setting
    e.g)
        {username}-{date}-{microsecond}{extension}
        hjh-2016-07-12-3333.png
    """
    return "{username}-{date}-{microsecond}{extension}".format(
        username=instance.user.username,
        date=str(now.date()),
        microsecond=now.microsecond,
        extension=os.path.splitext(filename)[1],
    )


def user_directory_path(instance, filename):
    """
    image upload directory setting
    e.g)
        images/{year}/{month}/{day}/{username}/{filename}
        images/2016/7/12/hjh/hjh-2016-07-12-158859.png
    """
    now = datetime.datetime.now()

    path = "images/{year}/{month}/{day}/{username}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        username=instance.user.username,
        filename=set_filename_format(now, instance, filename),
    )

    return path


class Experience(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    photo_job = models.ForeignKey("PhotoJobHistory")

    image = models.ImageField(
        upload_to=user_directory_path,
        blank=True,
        null=True,
    )

    content = models.CharField(
        max_length=100,
    )

    page = models.IntegerField()

    def __str__(self):
        return "{user_theme} - {hash_id} - {page}".format(
            user_theme=self.photo_job.user_theme,
            hash_id=self.photo_job.hash_id,
            page=self.page,
        )
