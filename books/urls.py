from django.urls import path
from . import views

urlpatterns = [
    path("ebooks", views.ebooks, name = "ebooks")
]