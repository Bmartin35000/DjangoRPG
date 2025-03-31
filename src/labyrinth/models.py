from django.db import models
from django.contrib.postgres.fields import ArrayField

class CaseType(models.TextChoices):
    WALL = "#"
    ENEMY = "X"
    PATH = " "
    CHEST = "O"

class Labyrinth(models.Model):
    cases = ArrayField(models.CharField(max_length=100)) # todo fix dependencies to use the arrayfield

    def __str__(self):
        return self.cases