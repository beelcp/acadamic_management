from . import views
from django.urls import path

urlpatterns = [
    path('admin_employee_add/',views.admin_employee_add,name="admin_employee_add"),
    path('get_subjects/',views.get_subjects, name='get_subjects'),
    path('admin_employee_adddbms/',views.admin_employee_adddbms,name="admin_employee_adddbms"),
    path('admin_employee_list/',views.admin_employee_list,name="admin_employee_list"),

    
]

