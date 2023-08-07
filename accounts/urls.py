from django.urls import path, include
from accounts.views import signup, user_login

urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", signup, name="signup"),
]
