from django import forms
from .models import ServiceRequest

class ServiceRequestForm(forms.ModelForm):
    class Meta:
        model = ServiceRequest
        fields = ['customer', 'vehicle, 'shop', 'description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'status': forms.Select(choices=ServiceRequest.STATUS_CHOICES)
        }
