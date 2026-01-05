from accounts.managers import CustomUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = models.CharField(verbose_name=_('username'), max_length=30, unique=True,null=True)
    email = models.EmailField(verbose_name=_("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    national_code = models.CharField(verbose_name=_('National Code'), max_length=20, unique=True)

    def __str__(self):
        return self.national_code