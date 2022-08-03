from django.db import models

# Create your models here.

class Book(models.Model):
    # creating fild (colums)
    title = models.CharField(max_length=50)
    rating = models.IntegerField()
    #Django will automatically create the ID column with autoincrement
    