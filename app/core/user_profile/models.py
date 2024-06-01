from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class Profile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True, blank=False, null=False)
    username = models.CharField(max_length=255, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, blank=False, null=True)
    last_name = models.CharField(max_length=255, blank=False, null=True)
    country = models.CharField(max_length=255, blank=False, null=True)
    city = models.CharField(max_length=255, blank=False, null=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    REQUIRED_FIELDS = ["username", "password", "is_staff"]

    USERNAME_FIELD = "email"
