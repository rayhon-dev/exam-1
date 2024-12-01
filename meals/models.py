from django.db import models

class Meal(models.Model):
    TYPE_CHOICES = [
        ('appetizer', 'Appetizer'),
        ('main course', 'Main Course'),
        ('dessert', 'Dessert'),
        ]
    meal_name = models.CharField(max_length=100)
    ingredients = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    type = models.CharField(max_length=20,choices=TYPE_CHOICES)
    cuisine = models.CharField(max_length=100)


