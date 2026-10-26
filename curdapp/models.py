
from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=20)
    age=models.PositiveIntegerField()
    email=models.EmailField()
    blood=models.CharField(max_length=20)
    def __str__(self):
        return self.name