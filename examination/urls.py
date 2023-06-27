from django.urls import path
from . import views

urlpatterns = [
    path("test", views.test, name="test"),
    path("exam", views.exam, name="exam"),
    path("result", views.result, name="result"),
    path("objective/explanation/<str:pk>", views.objectives_explanations, name = "objectives_explanations"),
    path("theory/explanation/<str:pk>", views.theory_explanations, name = "theory_explanations")
]