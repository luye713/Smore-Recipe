from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

class Grocery(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"grocery: {self.name}, amount: {self.amount}"
    def get_absolut_url(self):
        return reverse('grocery_list', kwargs={'pk': self.id})

class Equipment(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"equipment: {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"category: {self.name}"

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"name: {self.name}"
    def get_absolut_url(self):
        return reverse('recipe_detail', kwargs={'recipe_id': self.id})

class Ingredient(models.Model):
    text = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"ingredient: {self.text}"

class Instruction(models.Model):
    text = models.TextField(max_length=500)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"instruction: {self.text}"

class Comment(models.Model):
    text = models.TextField(max_length=1000)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"comment: {self.text}"
    def get_absolut_url(self):
        return reverse('home', kwargs={'comment_id': self.id})

class Trip(models.Model):
    name = models.CharField(max_length=50)
    start_date = models.DateField('Start day')
    end_date = models.DateField('End day')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"trip name: {self.name}"

    def get_absolut_url(self):
        return reverse('trip_detail', kwargs={'trip_id': self.id})

