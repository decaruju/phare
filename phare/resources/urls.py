from django.contrib import admin
from django.urls import path
from django.views.generic import ListView
from . import views
from resources.models import Ressource

urlpatterns = [
    path('', views.choisir_ressource, name="choix_ressource"),
]
