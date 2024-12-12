from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from .models import Member, Slider, Service, CallToAction
from .forms import MemberRegistrationForm, MemberLoginForm, MemberUpdateForm, PasswordResetForm, PasswordResetEmailForm



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


def member_list(request):

    members = Member.objects.all()
    return render(request, 'member/members_list.html', {'members': members})

def member_detail(request, pk):
    member = Member.objects.get(pk=pk)
    return render(request, 'member/members_detail.html', {'member': member})

def member_update(request, pk):
    member = get_object_or_404(Member, pk=pk)
    if request.method == "POST":
        form = MemberUpdateForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('Members:member_detail', pk=pk)
    else:
        form = MemberUpdateForm(instance=member)
    return render(request, 'member/members_update.html', {'form': form, 'member': member})
def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetEmailForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            request.session['reset_email'] = email  # Store email in session for later use
            return redirect('Members:password_reset_confirm')  # Redirect to the confirmation form

        else:
            messages.error(request, "Invalid email input.")
            return render(request, 'member/password_reset.html', {'form': form})

    else:
        form = PasswordResetEmailForm()
    return render(request, 'member/password_reset.html', {'form': form})

# Step 2: Show form to enter new password
def password_reset_confirm(request):
    email = request.session.get('reset_email')  # Retrieve the email from the session

    if not email:
        messages.error(request, "No email found for password reset. Please start over.")
        return redirect('Members:password_reset')  # Redirect to the email input form

    if request.method == 'POST':
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            new_password = form.cleaned_data.get('new_password')
            confirm_password = form.cleaned_data.get('confirm_password')

            try:
                member = Member.objects.get(email=email)
                if new_password == confirm_password:
                    member.password = make_password(new_password)  # Hash and save new password
                    member.save()
                    messages.success(request, "Your password has been updated successfully!")
                    request.session.pop('reset_email', None)  # Clear email from session
                    return redirect('Members:password_reset_success')  # Redirect to success page
                else:
                    messages.error(request, "Passwords do not match.")
            except Member.DoesNotExist:
                messages.error(request, "No account found with this email address.")

    else:
        form = PasswordResetForm()

    return render(request, 'member/password_reset_confirm.html', {'form': form, 'email': email})

# Step 3: Success page
def password_reset_success(request):
    return render(request, 'member/password_reset_success.html')