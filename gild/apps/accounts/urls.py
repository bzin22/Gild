from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django.views.generic.base import TemplateView

from . import views

app_name="accounts"

urlpatterns = [
    path('profile', views.ProfileView.as_view(), name="profile"),
    # Django Auth
    path('accounts/login', auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('accounts/logout', auth_views.LogoutView.as_view(), name="logout")
]
