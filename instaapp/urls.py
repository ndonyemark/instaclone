from django.urls import path, include
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('post_image', views.post_image, name='post_image')
]
