from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("question/<str:pk>", views.question, name = "question"),
    path("contact", views.contact, name="contact"),
    # ajax urls
    ]