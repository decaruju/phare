from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from ressources.models import Ressource

# Create your views here.

def choisir_ressource(request):
    return render(request, "choix_ressource.html")

def selection_ressource(request, choix):
    fields = {
        0: 'a_hebergement', 
        1: 'a_soins',
        2: 'a_transport',
        3: 'a_banque_alimentaire',
        4: 'a_assistance_psychologique',
        5: 'a_aide_financiere' 
	}
    kwargs = {fields[choix]: True}
    ressources = Ressource.objects.filter(**kwargs)
    context = RequestContext(request)
    context_dict = {'ressources': ressources, 'langue': request.LANGUAGE_CODE}
    return render_to_response('detail_ressources.html', context_dict, context)

def carte_ressources(request, choix):
    fields = {
        0: 'a_hebergement', 
        1: 'a_soins',
        2: 'a_transport',
        3: 'a_banque_alimentaire',
        4: 'a_assistance_psychologique',
        5: 'a_aide_financiere' 
	}
    kwargs = {fields[choix]: True}
    ressources = Ressource.objects.filter(**kwargs)
    context = RequestContext(request)
    context_dict = {'ressources': ressources, 'langue': request.LANGUAGE_CODE}
    return render_to_response('carte_ressources.html', context_dict, context)
