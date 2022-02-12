from tokenize import Triple
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from .models import User, Trip, Recipe, Ingredient, Instruction, Equipment
# from .forms import EquipmentForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# HOME
def home(request):
    return render(request, 'home.html')

def user_profile(request):
    return render(request, 'profile.html')

def signup(request):
    pass



# TRIP
def trip_list(request):
    return render(request, 'trip_list.html')

class trip_create(CreateView):
    pass
    # model = Trip
    # fields = ['name', 'destination', 'date', 'duration']

def trip_detail(request, trip_id):
    pass

class trip_delete(DeleteView):
    pass



# RECIPE
def recipe_category(request, trip_id):
    pass

def recipe_list(request, trip_id):
    pass

def recipe_detail(request, trip_id, recipe_id):
    pass

def recipe_save(request, trip_id, recipe_id):
    pass



# EQUIPMENT






