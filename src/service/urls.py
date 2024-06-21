from django.urls import path

from service.views import home

urlpatterns = [
    path('', home, name='dashboard'),
]