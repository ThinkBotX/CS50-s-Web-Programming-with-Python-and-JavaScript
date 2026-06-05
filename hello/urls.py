from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("anas", views.anas, name="anas"),
    path("ali", views.ali, name="ali")
]