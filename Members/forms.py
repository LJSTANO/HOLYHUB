from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member
from django.contrib.auth.models import User

class MemberRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    phone_number = forms.CharField(max_length=15, required=True)  # Set this field as required
    image = forms.ImageField(required=True)
    password1 = forms.CharField(widget=forms.PasswordInput, required=True)
    password2 = forms.CharField(widget=forms.PasswordInput, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone_number', 'password1', 'password2', 'image']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        # Save the Member's additional data, including image
        member = Member.objects.create(
            user=user,
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            phone_number=self.cleaned_data['phone_number'],
            image=self.cleaned_data.get('image')  # Store the image
        )

        return member

    from django import forms
    from django.contrib.auth.forms import AuthenticationForm

    class LoginForm(AuthenticationForm):
        # Optional: Add any custom fields or styling
        pass

