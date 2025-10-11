"""Defines URL patterns for main-app"""
from django.urls import path

from . import views

app_name = "mainapp"

urlpatterns = [
    # Home Page
    path("", views.index, name="index"),

    #Show all topics
    path('topics', views.topics, name='topics'),

    #Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic')
]