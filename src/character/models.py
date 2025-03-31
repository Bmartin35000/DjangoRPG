from django.db import models

# Create your models here.
class Character(models.Model):
    nom = models.CharField(max_length=50)
    niveau = models.IntegerField()
    classe = models.CharField(max_length=50)