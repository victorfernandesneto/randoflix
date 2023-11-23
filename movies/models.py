from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=200)
    watched = models.BooleanField(default=False)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return self.name
