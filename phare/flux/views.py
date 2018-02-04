from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from flux.models import Message
from flux.models import Citoyen


def index(request):
    return render(request, "accueil.html") 

def tous_messages(request):
    messages = Message.objects.order_by('-horodatage')[:10]
    context = RequestContext(request)
    context_dict = {'messages': messages, 'langue': request.LANGUAGE_CODE}
    return render_to_response('tous_messages.html', context_dict, context)


def vue_citoyen(request):
    citoyens = Citoyen.objects.order_by('-adresse')
    context = RequestContext(request)
    context_dict = {'citoyens': citoyens}
    return render_to_response('vue_citoyens.html', context_dict, context)
