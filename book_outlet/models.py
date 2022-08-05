from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import CharField
from django.urls import reverse


# Create your models here.

class Author(models.Model):
    first_name = CharField(max_length=100)
    last_name = CharField(max_length=100)


class Book(models.Model):
    # creating fild (colums)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    # CASCADE tells Django and SQL that if a author should be deleted any related book also should be deleted

    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # Django will automatically create the ID column with autoincrement

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
