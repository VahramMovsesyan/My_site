from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse


# Create your models here.


class Adress(models.Model):
    street = models.CharField(max_length=80)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=50)


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    adress = models.OneToOneField(Adress, on_delete=models.CASCADE, null=True)  # set up one-to-one relation

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name()


class Book(models.Model):
    # creating fild (colums)
    title = models.CharField(max_length=50)
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="books")
    # CASCADE tells Django and SQL that if a author should be deleted any related book also should be deleted

    is_bestselling = models.BooleanField(default=False)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)
    # Django will automatically create the ID column with autoincrement

    def get_absolute_url(self):
        return reverse("book-detail", args=[self.slug])

    def __str__(self):
        return f"{self.title} ({self.rating})"
