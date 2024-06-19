from django.db import models
from accounts.models import CustomUser


class Vehicle(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    problem_description = models.TextField()


class ServiceRequest(models.Model):
    PENDING = 'Pending'
    APPROVED = 'Approved'
    REPAIRING = 'Repairing'
    DONE = 'Done'
    RELEASED = 'Released'
    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (REPAIRING, 'Repairing'),
        (DONE, 'Done'),
        (RELEASED, 'Released'),
    ]

    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    shop = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Feedback(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shop = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Rating(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    shop = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
