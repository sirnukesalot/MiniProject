from django.urls import path
from . import views

urlpatterns = [
    path('post/all', views.all_posts, name='all_posts'),
    path('post/<int:pk>/', views.single_post, name='post_detail'),
    path('post/new', views.post_create, name='post_create'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),

]