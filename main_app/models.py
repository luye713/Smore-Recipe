from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


class Equipment(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"equipment: {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"category: {self.name}"

class Recipe(models.Model):
    name = models.CharField(max_length=20)
    categories = models.ManyToManyField(Category)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"name: {self.name}"

class Ingredient(models.Model):
    text = models.CharField(max_length=30)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"ingredient: {self.text}"

class Instruction(models.Model):
    text = models.TextField(max_length=200)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self):
        return f"instruction: {self.text}"


class Trip(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    start_date = models.DateField('Start day')
    end_date = models.DateField('End day')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"trip name: {self.name}, destination: {self.destination}"

