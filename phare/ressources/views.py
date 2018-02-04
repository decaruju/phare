from django.shortcuts import render

# Create your views here.

def choisir_ressource(request):
	return render(request, "choix_ressource.html.j2")
