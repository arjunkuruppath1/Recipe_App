from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):

    CATEGORY_CHOICES = [
        ("Starter", "Starter"),
        ("main courses", "main courses"),
        ("desserts", "desserts")
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()
    preparation_steps = models.TextField()
    cooking_time = models.IntegerField()
    serving_size = models.IntegerField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=25)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Rating(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

