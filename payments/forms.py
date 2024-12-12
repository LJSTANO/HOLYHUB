from django import forms
from .models import Payment
import re


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'payment_type', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')

        # Ensure the phone number starts with 254 and has 13 digits in total
        if not re.match(r'^254\d{9}$', phone_number):
            raise forms.ValidationError("Phone number must start with 254 and be 13 digits long.")

        return phone_number
