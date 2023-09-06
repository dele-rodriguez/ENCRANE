from django.urls import path
from . import views

urlpatterns =  [
    path("", views.home),
    path("myexams", views.myexams),
    path("questions/<str:id>", views.questions),
    path("add/<str:id>", views.addquestion)
]