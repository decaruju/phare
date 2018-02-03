from django.db import models


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


class Utilisateur(models.Model):
    nom = models.CharField(max_length=18)
    adresse = models.CharField(max_length=30)


class Autorite(models.Model):
    nom = models.CharField(max_length=18)
