from . import views
from django.urls import path

urlpatterns = [
    path('admin_employee_add/',views.admin_employee_add,name="admin_employee_add"),
    path('get_subjects/',views.get_subjects, name='get_subjects'),


    
]

