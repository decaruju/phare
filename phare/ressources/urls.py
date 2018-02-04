from django.contrib import admin
from django.urls import path
from django.views.generic import ListView
from . import views
from ressources.models import Ressource
from . import views

urlpatterns = [
    path('', views.choisir_ressource, name="choix_ressource"),
    path('/<int:choix>/', views.selection_ressource)
]
