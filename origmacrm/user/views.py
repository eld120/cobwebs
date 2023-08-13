from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeDoneView,
    PasswordChangeView,
)
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import User


# Create your views here.
class UserLoginView(LoginView):
    template_name = "user/login.html"


class UserLogoutView(LogoutView):
    pass


class UserDetailView(LoginRequiredMixin, DetailView):
    queryset = User.objects.all()
    template_name = "user/user_detail.html"

    class Meta:
        model = settings.AUTH_USER_MODEL


class UserPasswordChangeView(PasswordChangeView):
    pass


class UserPasswordChangeDoneView(PasswordChangeDoneView):
    pass
