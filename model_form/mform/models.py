from django.db import models


class Users(models.Model):
    Id = models.AutoField(primary_key=True)
    User_name = models.CharField(max_length=20)
    Email_Id = models.EmailField(max_length=30)
    Password = models.CharField(max_length=20)
