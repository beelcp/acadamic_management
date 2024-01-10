from . import views
from django.urls import path

urlpatterns = [
    path('admin_employee_add/',views.admin_employee_add,name="admin_employee_add"),



    
]

