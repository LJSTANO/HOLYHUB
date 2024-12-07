# forms.py
from django import forms
from .models import Member
from django.contrib.auth.hashers import check_password
from django.contrib.auth.forms import PasswordResetForm

class MemberRegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, required=True, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, required=True, label="Confirm Password")

    class Meta:
        model = Member
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data


class MemberLoginForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class CustomPasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label="Enter your email", required=True)

    class Meta:
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Please provide an email address.")
        return email