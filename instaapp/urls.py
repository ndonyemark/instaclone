from django.urls import path, include
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('post_image/', views.post_image, name='post_image'),
    path('single_image/<int:image_id>/', views.single_image_details, name='single_image'),
    path('search', views.search, name='search_results')
]
