from django.db import models

# Create your models here.

class Event(models.Model):

    nomeven = models.CharField(max_length=100)
    desceven= models.CharField(max_length=20, blank=True, null=True)  
    localisation = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'event'  # Nom de la table dans la base de données
    def __str__(self):
        return self.nomeven
class Participant(models.Model):
    nom = models.CharField(max_length=100)
    prenom= models.CharField(max_length=20, blank=True, null=True)  
    sexe= models.CharField(max_length=20, blank=True, null=True)  
    profession = models.CharField(max_length=100, blank=True, null=True)
    date_naissance = models.DateField(blank=True, null=True)


    def __str__(self):
        return self.nom