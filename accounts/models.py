from django.db import models


# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=35)
    holder = models.CharField(max_length=50)
    currency = models.CharField(max_length=20)
    locked = models.BooleanField()
    comment = models.CharField(max_length=50)
