from django.db import models


class User(models.Model):
    Id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)
