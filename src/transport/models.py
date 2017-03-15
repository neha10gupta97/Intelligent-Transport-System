from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Transport(models.Model):
    location=models.CharField(max_length=120)
