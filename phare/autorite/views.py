from django.shortcuts import render
from django import forms
from flux.models import TYPE_MESSAGE 
# Create your views here.
def autorite(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = MessageForm()
    return render(request, "autorite.html", {'form': form})


class MessageForm(forms.Form):
    titre_fr = forms.CharField()
    message_fr = forms.CharField(widget=forms.Textarea)
    titre_en = forms.CharField()
    message_en = forms.CharField(widget=forms.Textarea)
    message_type = forms.ChoiceField(choices=TYPE_MESSAGE, widget=forms.RadioSelect())

