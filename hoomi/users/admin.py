from django.contrib import admin
from users.models import User
from django.conf import settings


class UserAuthOption(admin.ModelAdmin):
    class Meta:
        model = settings.AUTH_USER_MODEL

admin.site.register(User, UserAuthOption)
