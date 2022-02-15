from dataclasses import field
from django.forms import ModelForm
from .models import Trip, Grocery

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'destination', 'start_date', 'end_date']

class GroceryForm(ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'amount']