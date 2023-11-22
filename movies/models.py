from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    watched = models.BooleanField(null=False, default=False)
    user = models.ForeignKey(
        to=User, on_delete=models.CASCADE, related_name='user')

    def __str__(self):
        return self.name
