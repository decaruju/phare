from django.contrib import admin
from django.urls import path
from django.views.generic import ListView
from . import views
from flux.models import Message

urlpatterns = [
    path('', views.autorite, name="autorite"),
]
