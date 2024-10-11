from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [

    path('register', views.register, name='register'),
    path('login', views.login_view, name="login"),
    path('user/<str:username>', views.profile_view, name='profile'),
    path('edit', views.profile_edit, name='profile_edit'),
    path('logout', views.logout_view, name = "logout"),
    # path('user/<str:username>/follow', views.follow_user, name='follow_user'),
    # path('user/<str:username>/unfollow', views.unfollow_user, name='unfollow_user')
]
