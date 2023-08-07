from django.urls import path, include
from accounts.views import signup, user_login, user_logout

urlpatterns = [
    path("login/", user_login, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", user_logout, name="logout"),
]
