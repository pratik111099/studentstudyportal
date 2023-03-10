from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('register/',views.UserRegistrationView, name='register'),
    path('activate/<uidb64>/<token>',views.activate, name='activate'),
    path('login/',auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="user/logout.html"), name='logout'),
    # path('logout/',views.UserSignOutView, name='logout'),
    path('profile/',views.ProfileView, name='profile'),
]
