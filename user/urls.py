from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(
        template_name='user/login.html'), name='user-login'),
    path('register', views.register, name='user-register'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='user/logout.html'), name='user-logout'),
    path('profile', views.profile, name='user-profile'),
    path('profile/update', views.profile_update, name='user-profile-update'),
]
