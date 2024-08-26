from django.db import models
from django.shortcuts import reverse
from django.utils.safestring import mark_safe

# Create your models here.

class Recipes(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField()
    cooking_time = models.FloatField()
    difficulty = models.CharField(max_length=20, blank=True)
    pic = models.ImageField(upload_to='Recipes', default='no_picture.jpg')

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse ( 'Recipes:recipedetail', kwargs={'pk': self.pk})

    def calculate_difficulty(self):
        ingredients = self.ingredients.split(", ")
        if self.cooking_time < 5 and len(ingredients) < 5:
            difficulty = "Easy"
        elif self.cooking_time < 5 and len(ingredients) >= 5:
            difficulty = "Medium"
        elif self.cooking_time >= 10 and len(ingredients) < 5:
            difficulty = "Intermediate"
        elif self.cooking_time >= 10 and len(ingredients) >= 5:
            difficulty = "Hard"
        return difficulty
