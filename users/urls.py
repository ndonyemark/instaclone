from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile_details', views.profile_setter, name='profile_details')
]
