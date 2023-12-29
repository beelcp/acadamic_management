from . import views
from django.urls import path
from .views import ajax_view,ajax_department_view


urlpatterns = [
    path('ad_department_manage/',views.admin_department_manage,name="admin_department_manage"),
    path('base',views.base,name="base"),
    path('ad_designation_manage',views.admin_designation_manage,name="admin_designation_manage"),
    path('ad_qualification_manage',views.admin_qualification_manage,name="admin_qualification_manage"),
    path('ad_class_manage',views.admin_class_manage,name="admin_class_manage"),
    path('ad_division_manage',views.admin_division_manage,name="admin_division_manage"),
    path('ad_employee_category',views.admin_employee_category,name="admin_employee_category"),
    path('ajaxsend/',ajax_view, name='ajaxsend'),
    path('ajax_department_view/', views.ajax_department_view, name='ajax_department_view'),

    
]

