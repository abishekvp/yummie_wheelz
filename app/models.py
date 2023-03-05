from django.db import models

class Models(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
    email = models.EmailField(max_length=30, unique=True)
    passwordusername = models.CharField(max_length=50)