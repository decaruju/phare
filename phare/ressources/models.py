from django.db import models

# Create your models here.
class Ressource(models.Model):
    nom = models.CharField(max_length=20)
    adresse = models.TextField()
    description_fr = models.TextField()
    description_en = models.TextField()

    a_hebergement = models.BooleanField()
    a_soins = models.BooleanField()
    a_biens_enssentiels = models.BooleanField()
    a_banque_alimentaire = models.BooleanField()
    a_assistance_psychologique = models.BooleanField()
    a_aide_financiere = models.BooleanField()
