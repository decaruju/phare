from django.shortcuts import render
from django.http import HttpResponse
from flux.models import Message


def index(request):
    return render(request, "accueil.html.j2") 

def tous_messages(request):
    messages = Message.objects.all().order_by('-horodatage')[:10]
    return render(request, "tous_messages.html.j2", messages.values()[0]) 

