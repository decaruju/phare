"""phare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import index, signup, profile, vue_citoyen

urlpatterns = [
    path('admin/', admin.site.urls),
    path('flux/', include('flux.urls')), 
    path('ressources/', include('ressources.urls')), 
    path('que-faire/', include('quefaire.urls')),
    path('autorite/', include('autorite.urls')),
    path('profile/', profile, name='profile'),
    path('vue_citoyens', vue_citoyen, name="vue_citoyen"),

    path('', index, name='accueil'), 
    path(r'i18n/', include('django.conf.urls.i18n'), name='changement_langue'),
    path(r'signup/', signup, name='signup'),
    path(r'login/', auth_views.login, name='login'),
    path(r'logout/', auth_views.logout, name='logout'),
]
