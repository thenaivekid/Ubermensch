from email.quoprimime import quote
from django.db import models

# Create your models here.
class Quotes(models.Model):
    quote = models.CharField(max_length=128)
    saidby = models.CharField(max_length=32)

    def __str__(self):
        return f"{self.quote} -{self.saidby}"
