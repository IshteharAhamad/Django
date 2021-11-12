from django.db import models


class User(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=20)
    Email = models.EmailField(max_length=30)
    Password = models.CharField(max_length=15)
