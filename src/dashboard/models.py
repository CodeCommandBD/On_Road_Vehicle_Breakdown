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


class CarRepairingType(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='site/', blank=True)


class BikeRepairingType(models.Model):
    title = models.CharField(max_length=255)
    icon = models.ImageField(upload_to='site/', blank=True)


class MembershipServices(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    services = models.JSONField()


class MembershipServicesType(models.Model):
    STATUS_CHOICES = [
        ('monthly', 'monthly'),
        ('year', 'year'),
    ]
    type = models.CharField(max_length=20, choices=STATUS_CHOICES, default='monthly')


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
