"""Defines URL patterns for main-app"""
from django.urls import path

from . import views

app_name = "mainapp"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),

    #Show all topics
    path(r'^topics/$', views.topics, name='topics')
]