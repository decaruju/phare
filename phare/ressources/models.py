from django.db import models

# Create your models here.
class Ressource(models.Model):
    nom = models.CharField(max_length=20)
    adresse = models.TextField()
    description_fr = models.TextField()
    description_en = models.TextField()

    disponibilite = models.BooleanField(default=1)

    latitude = models.DecimalField(max_digits=8, decimal_places=6, default=0.000000)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.000000)

    a_hebergement = models.BooleanField()
    a_soins = models.BooleanField()
    a_transport = models.BooleanField()
    a_banque_alimentaire = models.BooleanField()
    a_assistance_psychologique = models.BooleanField()
    a_aide_financiere = models.BooleanField()
