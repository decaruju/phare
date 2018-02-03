from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Dehors la ville doit être en feu') 
