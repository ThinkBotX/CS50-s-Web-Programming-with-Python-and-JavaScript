from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("anas", views.anas, name="anas"),
    path("ali", views.ali, name="ali")
]