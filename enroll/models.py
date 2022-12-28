from django.db import models

# Create your models here.
class User(models.Model): #This is the model
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)

    