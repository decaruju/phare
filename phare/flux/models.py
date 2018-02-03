from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

TYPE_BATIMENT = (
    ('r', 'résidentiel'),
    ('c', 'commercial'),
    ('b', 'bureau'),
    ('i', 'industriel'),
    ('p', 'public'),
)

TYPE_MESSAGE = (
        ('u','urgent'),
        ('n','normal'),
        ('i','info_general')
)
# Create your models here.
class Message(models.Model):
    auteur = models.CharField(max_length=18)
    horodatage = models.DateTimeField()
    titre_fr = models.CharField(max_length=20)
    titre_en = models.CharField(max_length=20)
    message_fr = models.TextField()
    message_en = models.TextField()
    type_message = models.CharField(max_length=1, choices=TYPE_MESSAGE)

class Citoyen(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Batiment(models.Model):
    adresse = models.CharField(max_length=30)
    code_postal = models.CharField(max_length=6)
    population = models.IntegerField(default=-1)
    mobilite_reduite = models.BooleanField()
    type_batiment = models.CharField(max_length=1, choices=TYPE_BATIMENT)
    gaz_naturel = models.BooleanField()
    propane = models.BooleanField()
    autre_danger = models.CharField(max_length=80)
