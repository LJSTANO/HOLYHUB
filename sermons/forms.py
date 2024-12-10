from django import forms
from .models import PrayerRequest

class PrayerRequestForm(forms.ModelForm):
    class Meta:
        model = PrayerRequest
        fields = ['name', 'email', 'phone_number', 'request']
        widgets = {
            'request': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Describe your prayer request here...'}),
        }
