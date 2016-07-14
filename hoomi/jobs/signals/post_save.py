from django.db.models.signals import post_save
from django.dispatch import receiver

from jobs.models import PhotoJobHistory


@receiver(post_save, sender=PhotoJobHistory)
def post_save_job_history(sender, instance, created, **kwargs):
    if created:
        from hashids import Hashids
        hashids = Hashids(salt="a!d34%", min_length=5)
        instance.hash_id = hashids.encode(instance.id)
        instance.save()
