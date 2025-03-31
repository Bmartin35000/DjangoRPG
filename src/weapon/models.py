from django.db import models

class WeaponType(models.TextChoices):
    HALLEBARDE = "Hallebarde"
    EPEE = "Epée"
    ARC = "Arc"
    BATON = "Baton"
    DAGUE = "Dague"
    FLEAU = "Fléau"
    EPEE_LONGUE = "Epée longue"

class Weapon(models.Model):
    type = models.CharField(choices= WeaponType.choices, max_length=50)
    degats = models.IntegerField()

    def __str__(self):
        return f"{self.type=} {self.degats=}"
    
