from django.contrib.auth.models import AbstractUser
from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='site/')
    icon = models.ImageField(upload_to='site/', blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=255, default='Set Email')
    address = models.CharField(max_length=255, default='Set Address')
    facebook_url = models.URLField(default='www.facebook.com')
    instagram_url = models.URLField(default='www.instagram.com')
    x_url = models.URLField(default='www.x.com')


class CustomUser(AbstractUser):
    profile_pic = models.ImageField(upload_to='user/')
    is_customer = models.BooleanField(default=False)
    is_shop = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    nid_image = models.ImageField(upload_to='user/', blank=True)
    experience = models.PositiveIntegerField(max_length=3, blank=True)
    no_of_workers = models.PositiveIntegerField(max_length=4, blank=True)
    have_membership = models.BooleanField(default=False)
