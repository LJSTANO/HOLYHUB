from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Event
from .forms import EventForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventAttendee

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('events:event_list')
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})


def register_attendee(request, event_id):
    event = get_object_or_404(Event, id=event_id)

    # Check if the user is already registered
    if EventAttendee.objects.filter(event=event, user=request.user).exists():
        messages.warning(request, 'You are already registered for this event.')
        return redirect('events:event_list')

    if request.method == 'POST':
        # Get form data
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        # Create an EventAttendee entry
        EventAttendee.objects.create(
            event=event,
            user=request.user,
            name=name,
            phone=phone,
            email=email
        )
        messages.success(request, 'Successfully registered for the event!')
        return redirect('events:event_list')

    return render(request, 'attendees.html', {'event': event})
def attendee_list(request):
    # Replace with actual logic to get attendees
    return render(request, 'attendees.html')