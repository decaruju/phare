from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "accueil.html") 

class SignupForm(ModelForm):
    username = forms.CharField()
    email = forms.EmailField()
    raw_password = forms.CharField(widget=forms.PasswordInput)
    Prénom = forms.CharField()
    last_name = forms.CharField()

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accueil')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

