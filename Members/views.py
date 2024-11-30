

from django.shortcuts import render,redirect
from pyexpat.errors import messages

from .models import Slider, Service, CallToAction
from django.contrib.auth.forms import AuthenticationForm
from .forms import forms

def index(request):
    service = Service.objects.all()
    slider = Slider.objects.all()
    call_to_action = CallToAction.objects.all()
    return render(request, 'member/index.html', {
        "slider": slider,
        "service": service,
        "call_to_action": call_to_action
    })
def login_view(request):
    form = AuthenticationForm()  # Ensure you're using the correct form class
    return render(request, 'member/login.html', {'form': form})

def password_reset(request):
    return render(request,'member/password_reset.html')

from django.shortcuts import render, redirect
from .forms import MemberRegistrationForm

def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST, request.FILES)  # Add request.FILES here
        if form.is_valid():
            form.save()

            messages.success(request, 'Registration successful! You can now login.')
            return redirect('member:index')  # Adjust the redirect URL as needed
    else:
        form = MemberRegistrationForm()
    return render(request, 'register/register.html', {'form': form})