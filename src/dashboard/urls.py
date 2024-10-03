from django.urls import path

from dashboard.views import dashboard

from accounts.views import staff_login_view



from dashboard.views import *

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('login/', staff_login_view, name="staff_login_view"),
    path('logout/', staff_logout, name="staff_logout"),
    path('sites/', site_list, name='site_list'),
    path('sites/create/', site_create, name='site_create'),
    path('sites/update/', site_update, name='site_update'),

]