from django.urls import path
from . import views

urlpatterns = [
    path('', views.billing_list, name='billing_list'),
    path('create/', views.create_billing, name='create_billing'),
    path('edit/<int:pk>/', views.edit_billing, name='edit_billing'),
    path('delete/<int:pk>/', views.delete_billing, name='delete_billing'),
]
