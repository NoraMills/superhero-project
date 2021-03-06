from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_superpower = models.CharField(max_length=50)
    secondary_superpower = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)

    def __str__(self):
        return self.name
