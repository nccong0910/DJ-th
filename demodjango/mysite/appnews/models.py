from django.db import models


# Create your models here.

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name  = models.CharField(max_length=50)

class ProfileUser(models.Model):
    address = models.CharField(max_length= 200)
    phone = models.IntegerField()
    avatar = models.ImageField()