from unicodedata import name
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    price = models.FloatField()
    published = models.DateField()
    desc=models.TextField()

    def __str__(self):
        return self.title
        
class Admin(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique=True)
    def __str__(self):
        return self.name        
