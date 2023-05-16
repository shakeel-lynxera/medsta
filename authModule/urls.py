from django.urls.conf import path
from authModule import views


urlpatterns = [
    path("login/", views.login, name="user-login"),
    path("registration/", views.registration, name="user-registration"),
    path("registration-otp-verification/", views.registration_otp_verification, name="user-registration-otp-verification"),
    path("forget-password/", views.forget_password, name="user-forget-password"),
    path("verify-forget-password-otp/", views.verify_forget_password_otp, name="user-forget-password"),
    path("reset-password/", views.reset_password, name="user-reset-password"),
]