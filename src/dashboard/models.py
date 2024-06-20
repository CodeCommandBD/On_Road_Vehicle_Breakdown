from django.db import models

from accounts.models import CustomUser


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


class Blog(models.Model):
    PENDING = 'Pending'
    REPAIRING = 'Repairing'
    DONE = 'Done'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (REPAIRING, 'Repairing'),
        (DONE, 'Done'),
    ]
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.TextField(max_length=10000)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)


class TrafficRule(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class DrivingInstruction(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
