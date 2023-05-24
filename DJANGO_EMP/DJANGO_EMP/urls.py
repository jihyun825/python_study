"""
URL configuration for DJANGO_EMP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from DJANGO_EMP import views

urlpatterns = [
    path('emp_list',views.emplist),
    path('',views.emplist),
    path('emp_detail',views.empdetail),
    path('emp_mod',views.empmod),
    path('emp_mod_act',views.empmodact),
    path('emp_add',views.empadd),
    path('emp_add_act',views.empaddact),
    path('emp_del_act',views.empdelact),
]
