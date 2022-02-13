from django.contrib import admin
from .models import Trip, Recipe, Equipment, Category, Ingredient, Instruction

# Register your models here.
admin.site.register(Trip)
admin.site.register(Recipe)
admin.site.register(Equipment)
admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Instruction)