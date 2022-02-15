from dataclasses import field
from django.forms import ModelForm
from .models import Trip, Grocery, Comment

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'start_date', 'end_date']

class GroceryForm(ModelForm):
    class Meta:
        model = Grocery
        fields = ['name', 'amount']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']