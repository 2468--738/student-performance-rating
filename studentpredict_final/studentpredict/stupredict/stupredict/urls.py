"""stupredict URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('home/', views.home),
    path('insert/', views.insert),
    path('update/', views.update),
    path('delete/', views.delete),
    path('contacts/', views.contact),
    path('predict_students/', views.predict_students),
    path('predict_given/', views.predict_given),
    path('add_student/<int:roll>/', views.add_student),
    path('remove_student/<int:roll>/', views.remove_student),
    path('delete_students/', views.delete_students),
    path('delete_given_student/<int:stu_id>', views.delete_given_student),
    path('delete_branch/', views.delete_branch),
    path('delete_given_branch/<int:roll>', views.delete_given_branch),
    path('delete_subject/', views.delete_subject),
    path('delete_given_subject/<str:sub_code>', views.delete_given_subject),
    path('delete_offer/', views.delete_offer),
    path('delete_given_offer/<int:off_id>', views.delete_given_offer),
    path('delete_performance/', views.delete_performance),
    path('delete_given_performance/<int:per_id>', views.delete_given_performance),
    path('delete_test/', views.delete_test),
    path('delete_given_test/<int:test_id>', views.delete_given_test),
    path('update_student/', views.update_student),
    path('update_given_student/<int:stu_id>', views.update_given_student),
    path('update_subject/', views.update_subject),
    path('update_given_subject/<str:sub_code>', views.update_given_subject),
    path('update_performance/', views.update_performance),
    path('update_given_performance/<int:roll>', views.update_given_performance),
    path('insert_session/', views.insert_session),
    path('insert_student/', views.insert_student),
    path('insert_branch/', views.insert_branch),
    path('insert_subject/', views.insert_subject),
    path('insert_attendance/', views.insert_attendance),
    path('insert_test/', views.insert_test),
    path('insert_mock/', views.insert_mock),
    path('insert_performance/', views.insert_performance),
    path('insert_job/', views.insert_job),
]
