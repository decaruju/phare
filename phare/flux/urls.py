from django.contrib import admin
from django.urls import path
from django.views.generic import ListView
from flux.models import Message
from . import views

urlpatterns = [
    path('', views.tous_messages, name="flux"),
]
