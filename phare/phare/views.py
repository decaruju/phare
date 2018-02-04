from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponse
from flux.models import Message
from django import forms
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, "accueil.html") 

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

