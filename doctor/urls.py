from django.urls import path
from . import views

urlpatterns = [
    path('', views.doctors_list, name='doctors_list'),
    path('register/', views.register_doctor, name='register_doctor'),
    path('edit/<int:doctor_id>/', views.edit_doctor, name='edit_doctor'),
    path('delete/<int:doctor_id>/', views.delete_doctor, name='delete_doctor'),
]