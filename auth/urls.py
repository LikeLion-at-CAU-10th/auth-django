from django.urls import path
from .views import *

urlpatterns = [
    path("login", login_view, name="auth-login"),
    path("logout", logout_view, name="auth-logout"),
]
