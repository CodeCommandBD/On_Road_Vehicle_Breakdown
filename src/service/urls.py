from django.urls import path

from service.views import *

urlpatterns = [
    path('', home, name='home'),
    path('sign-up/', userSignUp, name='userSignUp'),
    path('login/', userLogin, name='userLogin'),
]