from django.shortcuts import render
from django.forms import ModelForm
from flux.models import TYPE_MESSAGE, Message
# Create your views here.
def autorite(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            # add logged user
            form.save()
    else:
        form = MessageForm()
    return render(request, "autorite.html", {'form': form})


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['titre_fr','message_fr','titre_en','message_en','type_message']
