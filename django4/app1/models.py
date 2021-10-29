from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=2)
    value = models.CharField(max_length=6)
    class Meta:
        unique_together = (("user", "location"))
