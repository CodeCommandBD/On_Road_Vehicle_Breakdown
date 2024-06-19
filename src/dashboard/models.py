from django.db import models

from accounts.models import CustomUser


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