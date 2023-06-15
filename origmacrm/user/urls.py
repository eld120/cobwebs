from django.urls import path

from . import views

app_name = "user"

urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", views.UserLogoutView.as_view(), name="logout"),
    path(
        "password-change/",
        views.UserPasswordChangeView.as_view(),
        name="password_change",
    ),
    path(
        "password-change/done/",
        views.UserPasswordChangeDoneView.as_view(),
        name="password_change_done",
    ),
    # path("~redirect/", view=user_redirect_view, name="redirect"),
    # path("~update/", view=user_update_view, name="update"),
    # path("<str:username>/", view=user_detail_view, name="detail"),
]
