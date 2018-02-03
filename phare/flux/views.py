from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from flux.models import Message


def index(request):
    return render(request, "accueil.html.j2") 

def tous_messages(request):
    messages = Message.objects.order_by('-horodatage')[:10]
    context = RequestContext(request)
    context_dict = {'messages': messages}
    return render_to_response('tous_messages.html.j2', context_dict, context)

