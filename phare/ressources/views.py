from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from ressources.models import Ressource

# Create your views here.

def choisir_ressource(request):
    ressources = Ressource.objects.all()
    context = RequestContext(request)
    context_dict = {'ressources': ressources, 'langue': request.LANGUAGE_CODE}
    return render_to_response("choix_ressource.html", context_dict, context)


def detail_ressource(request):

	return render_to_response(request, "choix_ressource.html")
