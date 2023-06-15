from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.shortcuts import render


# Create your views here.
class UserLoginView(LoginView):
    template_name = "user/login.html"


class UserLogoutView(LogoutView):
    pass


class UserPasswordChangeView(PasswordChangeView):
    pass


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    pass
