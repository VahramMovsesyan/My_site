from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.

class Book(models.Model):
    # creating fild (colums)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.CharField(null=True, max_length=100)
    is_bestselling = models.BooleanField(default=False)
    #Django will automatically create the ID column with autoincrement

    def get_absolute_url(self):
        return reverse("model_detail", args=[self.id])
    

    def __str__(self):
        return f"{self.title} ({self.rating})"
