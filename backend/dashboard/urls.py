from django.urls import path, include

from dashboard.views import dashboard_view, check_login_status

urlpatterns = [
    path('', dashboard_view, name='dashboard'),
    path('check-login-status/', check_login_status, name='check_login_status'),

]
