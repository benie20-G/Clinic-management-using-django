from django.urls import path,include
from . import views

urlpatterns = [
    path('rec/', include('medicalrecords.urls')),
    path('', views.appointment_list, name='appointment_list'),
    path('create/', views.create_appointment, name='create_appointment'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
]
