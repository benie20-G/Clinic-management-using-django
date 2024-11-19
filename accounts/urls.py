from django.urls import path
from . import views
from patients.views import index

urlpatterns = [
     path('dashboard/', index, name='index'),
    path('', views.signup, name='signup'),
      path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Ensure you create a logout view in views.py
]
