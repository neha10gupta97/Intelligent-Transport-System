from __future__ import unicode_literals

from django.db import models

# Create your models here.
class user_details(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=120)

    def __unicode__(self):
        return self.username

#class Profile