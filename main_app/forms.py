from django.forms import ModelForm
from .models import Trip

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = ['name', 'start_date', 'end_date', 'destination']