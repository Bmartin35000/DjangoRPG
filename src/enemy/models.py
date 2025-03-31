from django.db import models

class EnemyType(models.TextChoices):
    GOBELIN = "Gobelin"
    ORC = "Orc"
    OGRE = "Ogre"
    CENTAURE = "Centaure"
    DRAGON = "Dragon"

class Enemy(models.Model):
    type = models.CharField(max_length=50, choices=EnemyType)
    degats = models.IntegerField()
    pv = models.IntegerField()

    def __str__(self):
        return f"{self.type=} {self.degats=} {self.pv=}"