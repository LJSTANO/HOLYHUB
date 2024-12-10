
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
from Members.models import Member
from .forms import NewsletterForm
from .models import Newsletter

def send_newsletter(request):
    if request.user.is_staff:  # Ensure only admin can access
        if request.method == 'POST':
            form = NewsletterForm(request.POST)
            if form.is_valid():
                # Save the newsletter to the database
                newsletter = form.save()

                # Fetch all member emails from the database
                recipient_list = [member.email for member in Member.objects.all()]

                # Send the email to all recipients
                subject = newsletter.subject
                message = newsletter.content
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)

                # Send confirmation email to the admin
                send_mail(
                    'Newsletter Sent Successfully',
                    f'The newsletter "{newsletter.subject}" has been sent to all members.',
                    settings.EMAIL_HOST_USER,
                    [settings.DEFAULT_ADMIN_EMAIL],
                )

                # Redirect to a success page
                return redirect('newsletter_sent')
        else:
            form = NewsletterForm()

        return render(request, 'newsletter_form.html', {'form': form})
    else:
        return redirect('no_permission')  # If user is not an admin

def newsletter_sent(request):
    return render(request, 'newsletter_sent.html')

def newsletter_sent(request):
    return render(request, 'newsletter_sent.html')

def no_permission(request):
    return render(request, 'no.html')
