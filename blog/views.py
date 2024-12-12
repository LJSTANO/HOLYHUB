from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from django.contrib import messages

def testimonials (request):
    return render(request,'testimonials.html')


def pricing(request):
    return render(request, 'pricing.html')

def contact(request):
    return render(request, 'contact.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('blog:thank_you')  # Redirect to a thank-you page
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

def thank_you_view(request):
    return render(request, "thank_you.html")
