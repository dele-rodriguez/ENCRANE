from django.urls import path
from . import views

urlpatterns = [
    path("register", views.register, name = "register"),
    path("dashboard", views.dashboard, name = "dashboard"),
    path("login", views.login_, name = "login"),
    path("logout", views.logout_, name = "logout")
]