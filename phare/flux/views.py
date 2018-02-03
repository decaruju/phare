from django.shortcuts import render
from django.http import HttpResponse
from flux.models import Message


def index(request):
    messages = Message.objects.all.orderby('-date')[:10]
    return render(request, "accueil.html.j2", messages) 
