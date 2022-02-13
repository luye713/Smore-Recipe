from unicodedata import category
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Trip, Recipe, Ingredient, Instruction, Equipment, Category
from .forms import TripForm

# HOME
def home(request):
    categories = Category.objects.all()
    equipments = Equipment.objects.all()
    recipes = Recipe.objects.all()

    return render(request, 'home.html', {
        'categories': categories,
        'equipments': equipments,
        'recipes': recipes
    })
    

@login_required
def user_profile(request):
    return render(request, 'profile.html')

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)



# TRIP
class trip_list(LoginRequiredMixin, ListView):
    model = Trip

class trip_create(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['name', 'destination', 'start_date', 'end_date']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class trip_detail(LoginRequiredMixin, DetailView):
    model = Trip

class trip_delete(LoginRequiredMixin, DeleteView):
    model = Trip
    success_url = '/trips/'



# RECIPE
@login_required
def recipe_list(request, trip_id):
    pass

@login_required
def recipe_detail(request, trip_id, recipe_id):
    pass

@login_required
def recipe_save(request, trip_id, recipe_id):
    pass



# EQUIPMENT






