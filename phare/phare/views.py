from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.conf import settings
from django.contrib.auth.models import User


def index(request):
    return render(request, "accueil.html") 

class SignupForm(ModelForm):
    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        fields = '__all__'
        exclude = [
                'groups',
                'last_login',
                'user_permissions',
                'is_staff',
                'is_active',
                'is_superuser',
                'date_joined'
        ]
        widgets = {
                'password': forms.PasswordInput()
        }

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('accueil')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

