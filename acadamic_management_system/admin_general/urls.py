from . import views
from django.urls import path

urlpatterns = [
    path('base',views.base,name="base"),
    path('blank',views.blank,name="blank"),



    
]

