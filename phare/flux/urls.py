from django.contrib import admin
from django.urls import path
from django.views.generic import ListView
from . import views
from flux.models import Message

urlpatterns = [
    path('', views.tous_messages, name="flux"),
	path('vue_citoyens', views.vue_citoyen, name="vue_citoyen"),
]
