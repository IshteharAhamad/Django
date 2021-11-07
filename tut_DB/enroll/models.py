from django.db import models


class Student(models.Model):
    s_id = models.IntegerField(primary_key=True)
    roll_No = models.IntegerField()
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    mobile = models.IntegerField()
    course = models.CharField(max_length=20, default="availble here")

    # def __str__(self):
    #    return self.name
