"""
URL configuration for administrative_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app1.views import (register_form,login1_form,home,department_table,department_empty_form,department_update_form,department_delete,
                      hod_table,hod_empty_form,hod_update_form,hod_delete,professor_table,professor_empty_form,professor_update_form,professor_delete,
                      student_table,student_empty_form,student_update_form,student_delete,verify_user)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path("",login1_form,name="log101"),
    path("reg101/",register_form,name="reg101"),
    path("home101/",home,name='home101'),
    path("verify/<str:action>/<int:id>/",verify_user,name="verify_user"),

    path("dept_table101/",department_table,name='dept_table101'),
    path("dept_form101/",department_empty_form,name='dept_form101'),
    path("dept_form101/<int:id>/",department_update_form,name='dept_form102'),
    path("dept_delete101/<int:id>/",department_delete,name='dept_delete101'),

    path("hod_table101/",hod_table,name='hod_table101'),
    path("hod_form101/",hod_empty_form,name='hod_form101'),
    path("hod_form102/<int:id>/",hod_update_form,name='hod_form102'),
    path("hod_delete101/<int:id>/",hod_delete,name='hod_delete101'),

    path("professor_table101/",professor_table,name='professor_table101'),
    path("professor_form101/",professor_empty_form,name='professor_form101'),
    path("professor_form102/<int:id>/",professor_update_form,name='professor_form102'),
    path("professor_delete101/<int:id>/",professor_delete,name='professor_delete101'),

    path("student_table101/",student_table,name='student_table101'),
    path("student_form101/",student_empty_form,name='student_form101'),
    path("student_form102/<int:id>/",student_update_form,name='student_form102'),
    path("student_delete101/<int:id>/",student_delete,name='student_delete101'),
]

