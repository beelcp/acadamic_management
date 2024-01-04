from . import views
from django.urls import path
from .views import ajax_view


urlpatterns = [


    path('base',views.base,name="base"),
    path('ajaxsend/',ajax_view, name='ajaxsend'),


    path('ad_department_manage/', views.admin_department_manage, name='admin_department_manage'),
    path('ajax_department_view/', views.ajax_department_view, name='ajax_department_view'),
    path('ajax_department_update/', views.ajax_department_update, name='ajax_department_update'),
    path('ajax_delete_row1/', views.ajax_delete_row1, name='ajax_delete_row1'),


    path('ad_designation_manage', views.admin_designation_manage, name='admin_designation_manage'),
    path('ajax_designation_view/', views.ajax_designation_view, name='ajax_designation_view'),
    path('ajax_designation_update/', views.ajax_designation_update, name='ajax_designation_update'),
    path('ajax_delete_desrow1/', views.ajax_delete_desrow1, name='ajax_delete_desrow1'),


    path('ad_qualification_manage', views.admin_qualification_manage, name='admin_qualification_manage'),
    path('ajax_qualification_view/', views.ajax_qualification_view, name='ajax_qualification_view'),
    path('ajax_qualification_update/', views.ajax_qualification_update, name='ajax_qualification_update'),
    path('ajax_delete_qualification_row/', views.ajax_delete_qualification_row, name='ajax_delete_qualification_row'),


    path('ad_class_manage', views.admin_class_manage, name='admin_class_manage'),
    path('ajax_class_view/', views.ajax_class_view, name='ajax_class_view'),
    path('ajax_class_update/', views.ajax_class_update, name='ajax_class_update'),
    path('ajax_delete_class_row/', views.ajax_delete_class_row, name='ajax_delete_class_row'),


    path('ad_division_manage', views.admin_division_manage, name='admin_division_manage'),
    path('ajax_division_view/', views.ajax_division_view, name='ajax_division_view'),
    path('ajax_division_update/', views.ajax_division_update, name='ajax_division_update'),
    path('ajax_delete_divsrow/', views.ajax_delete_divsrow, name='ajax_delete_divsrow'),


    path('ad_employee_category', views.admin_employee_category, name='admin_employee_category'),
    path('ajax_employee_category_view/', views.ajax_employee_category_view, name='ajax_employee_category_view'),
    path('ajax_employee_category_update/', views.ajax_employee_category_update, name='ajax_employee_category_update'),
    path('ajax_delete_employee_row/', views.ajax_delete_employee_row, name='ajax_delete_employee_row'),


]