
from django import forms
from .models import Event,EventsAttendee

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'event_date']


class EventsAttendeeForm(forms.ModelForm):
    class Meta:
        model = EventsAttendee
        fields = ['name', 'email', 'event']  # Assuming event is passed with the URL
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }