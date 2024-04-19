from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views


app_name = "users"


urlpatterns = [
    path("signup/", views.signupuser, name="signup"),
    path("login/", views.loginuser, name="login"),
    path("logout/", views.logoutuser, name="logout"),
    path("profile/", views.profile, name="profile"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path("password_reset/", PasswordResetView.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>/", PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]