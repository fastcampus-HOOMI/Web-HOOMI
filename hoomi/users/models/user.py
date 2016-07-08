from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db import models
from jobs.models import Job


class UserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        user = self.model(
                email=self.normalize_email(email),
                **kwargs,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **kwargs):
        user = self.create_user(
                email=self.normalize_email(email),
                **kwargs
        )
        user.is_superuser=True
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)


class User(AbstractBaseUser, PermissionsMixin):
    job = models.ForeignKey(Job)
    name = models.CharField(
            max_length=60,
    )
    email = models.EmailField(
            unique=True,
    )
    USERNAME_FIELD = 'email'

    objects = UserManager()
    
    # under lines for admin
    is_admin = models.BooleanField(default=False)
    def get_short_name(self):
        return self.name

    @property
    def is_staff(self):
        return self.is_admin
    

    def __str__(self):
        return self.email
