from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(max_length=254,unique=True)
    city = models.CharField(max_length=101, null=True, blank=True)

    def __str__(self):
        return self.name
