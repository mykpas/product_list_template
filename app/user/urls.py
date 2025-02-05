from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('profile', views.profile, name='profile'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register', views.register, name='register'),
]
