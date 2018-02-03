from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from address.models import AddressField

TYPE_MESSAGE = (
        ('u','urgent'),
        ('n','normal'),
        ('i','info_general')
)
# Create your models here.
class Message(models.Model):
    auteur = models.CharField(max_length=18)
    horodatage = models.DateTimeField()
    message_fr = models.TextField()
    message_en = models.TextField()
    type_message = models.CharField(max_length=1, choices=TYPE_MESSAGE)

class Citoyen(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    adresse = models.CharField(max_length=30)

class Batiment(models.Model):
    adresse
