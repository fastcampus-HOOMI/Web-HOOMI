from django.apps import AppConfig


class JobAppConfig(AppConfig):
    name = "jobs"

    def ready(self):
        from jobs.signals.post_save import post_save_job_history
