from __future__ import unicode_literals

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin, AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import BaseUserManager
# Create your models here.
from standard_django import settings


class User(AbstractUser):
    profile_name = models.CharField(_('profile_name'), max_length=30, blank=True)
    contact_number = models.CharField(max_length=30, blank=True, null=True)
    is_deleted = models.BooleanField('delete', default=False,)
    image = models.ImageField(upload_to=settings.MEDIA_USER_IMAGE, blank=True, null=True, default="")