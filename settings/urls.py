from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Register
    path(
        'register/',
        views.register_view,
        name='register'
    ),
    # Login
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name = 'auth/login.html'
        ), name='login'
    ),
    # Logout
    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'),
    # Profiles
    path(
        'profile/',
        views.profile_view,
        name='profile'
    )
]