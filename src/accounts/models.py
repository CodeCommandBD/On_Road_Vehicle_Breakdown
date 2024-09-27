from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='user/')
    is_customer = models.BooleanField(default=False)
    is_shop = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    nid_image = models.ImageField(upload_to='user/', blank=True)
    experience = models.PositiveIntegerField(blank=True, null=True)
    no_of_workers = models.PositiveIntegerField(blank=True, null=True)
    have_membership = models.BooleanField(default=False)
