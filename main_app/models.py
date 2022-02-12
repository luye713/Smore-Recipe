
from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User
from django_better_admin_arrayfield.models.fields import ArrayField
from django_better_admin_arrayfield.admin.mixins import DynamicArrayMixin

# Create your models here.


class Equipment(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"name: {self.name}"

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return f"name: {self.name}"

class Recipe(models.Model, DynamicArrayMixin):
    name = models.CharField(max_length=20)
    ingredient = ArrayField(models.CharField(max_length=30))
    instruction = ArrayField(models.CharField(max_length=200))
    categories = models.ManyToManyField(Category)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"name: {self.name}"


class Trip(models.Model):
    name = models.CharField(max_length=20)
    destination = models.CharField(max_length=50)
    start_date = models.DateField('Start day')
    end_date = models.DateField('End day')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipe)
    equipments = models.ManyToManyField(Equipment)

    def __str__(self):
        return f"name: {self.name}"


