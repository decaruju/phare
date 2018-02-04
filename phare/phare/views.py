from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from flux.models import Message


def index(request):
    return render(request, "accueil.html") 
