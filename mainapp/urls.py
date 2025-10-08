"""Defines URL patterns for main-app"""
from django.urls import path

from . import views

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),
]