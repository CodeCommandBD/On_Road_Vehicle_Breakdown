from django.urls import path

from dashboard.views import dashboard

from accounts.views import staff_login_view

from dashboard.views import staff_logout

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', staff_login_view, name="staff_login_view"),
    path('logout/', staff_logout, name="staff_logout"),

]