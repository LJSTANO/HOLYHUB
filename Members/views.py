from django.shortcuts import render,redirect
from .models import Slider, Service, CallToAction
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .forms import MemberRegistrationForm, MemberLoginForm,PasswordResetForm
from .models import Member


def index(request):
    service = Service.objects.all()
    slider = Slider.objects.all()
    call_to_action = CallToAction.objects.all()
    return render(request, 'member/index.html', {
        "slider": slider,
        "service": service,
        "call_to_action": call_to_action
    })
# Registration view
def register(request):
    if request.method == 'POST':
        form = MemberRegistrationForm(request.POST)
        if form.is_valid():
            # Save the member with a hashed password
            member = form.save(commit=False)
            member.password = make_password(form.cleaned_data['password1'])
            member.save()
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('Members:login')  # Use the 'Members' namespace

    else:
        form = MemberRegistrationForm()
    return render(request, 'member/register.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = MemberLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                member = Member.objects.get(username=username)
                if check_password(password, member.password):
                    # Login successful
                    request.session['member_id'] = member.id
                    messages.success(request, f'Welcome {member.first_name}!')
                    return redirect('Members:index')  # Replace 'home' with your dashboard URL
                else:
                    messages.error(request, 'Invalid username or password.')
            except Member.DoesNotExist:
                messages.error(request, 'Invalid username or password.')

    else:
        form = MemberLoginForm()
    return render(request, 'member/login.html', {'form': form})

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(request=request)
            messages.success(request, 'A password reset link has been sent to your email.')
            return redirect('Members:login')  # Redirect to the login page after request
    else:
        form = PasswordResetForm()

    return render(request, 'Member/password_reset.html', {'form': form})
