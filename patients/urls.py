from django.urls import path
from . import views

urlpatterns = [
    path('', views.patient_list, name='patient_list'),
    path('create/', views.create_patient, name='create_patient'),
     path('edit/<int:patient_id>/', views.edit_patient, name='edit_patient'),
      path('delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),  # Add this line

]
