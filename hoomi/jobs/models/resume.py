import datetime
import os

from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.db import models


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

    path = "images/{year}/{month}/{day}/resume/{username}/{filename}".format(
        year=now.year,
        month=now.month,
        day=now.day,
        username=instance.user.username,
        filename=set_filename_format(now, instance, filename),
    )

    return path


class Resume(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    user_image = models.ImageField(
        upload_to=user_directory_path,
    )

    # Side Bar
    github_profile = models.URLField()
    name = models.CharField(
        max_length=30
    )
    detail_job = models.CharField(
        max_length=40
    )

    # Profile_Timeline
    timeline_name = models.TextField()
    timeline_job = models.TextField()
    timeline_description = models.TextField()

    # Personal_Info
    profile_name = models.CharField(
        max_length=50
    )
    profile_birth = models.DateField(
        blank=True,
        null=True,
    )
    profile_email = models.EmailField()
    profile_address = models.TextField()
    profile_phone = models.TextField()
    profile_blog = models.URLField(
        blank=True,
        null=True,
    )

    # Experience
    experiences = JSONField(
        blank=True,
        null=True,
    )

    # education
    educations = JSONField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name
