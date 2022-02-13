from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User, Trip, Recipe, Ingredient, Instruction, Equipment
from .forms import TripForm

# HOME
def home(request):
    return render(request, 'home.html')

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
@login_required
def trip_list(request):
    trips = Trip.objects.filter(user=request.user)
    return render(request, 'main_app/trip_list.html', { 'trips': trips })

class trip_create(LoginRequiredMixin, CreateView):
    model = Trip
    fields = ['name', 'destination', 'start_date', 'end_date']
    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

@login_required
def trip_detail(request, trip_id):
    trip = Trip.objects.filter(id=trip_id, user=request.user)
    return render(request, 'main_app/trip_detail.html', { 'trip': trip })

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






