from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from ressources.models import Ressource

# Create your views here.

def que_faire(request):
	return render(request, 'que_faire.html')


def que_faire_detail(request, sujet):
	if(sujet=='innondation'):
		return render(request, 'innondation.html')
