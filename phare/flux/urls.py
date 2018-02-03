from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('/tous-les-messages', views.tous_messages, name="tous_messages"),

]
