from django.db import models
from weapon.models import Weapon

class RaceType(models.TextChoices):
    NAIN = "Nain"
    ELFE = "Elfe"
    HUMAIN = "Humain"

class Character(models.Model):
    nom = models.CharField(max_length=50)
    niveau = models.IntegerField(default=1)
    race = models.CharField(max_length=50, choices=RaceType)
    pv = models.IntegerField(default=100)
    arme = models.OneToOneField(Weapon, on_delete=models.CASCADE, null=True, blank=True) # null set null as default, blank makes field optional
    numLigne = models.IntegerField(null=True, blank=True)
    numColonne = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.nom=} {self.niveau=} {self.classe=}"