from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Event, EventsAttendee
from .forms import EventForm, EventsAttendeeForm

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

def attendees_list(request):
    events = Event.objects.all()
    return render(request, 'attendees_list.html', {'events': events})


def confirm_attendance(request, event_id):

    event = get_object_or_404(Event, id=event_id)

    if request.method == 'POST':

        form = EventsAttendeeForm(request.POST)
        if form.is_valid():

            attendee = form.save(commit=False)
            attendee.event = event
            attendee.save()
            return redirect('events:attendees')  # Redirect to the list of attendees
    else:

        form = EventsAttendeeForm()

    return render(request, 'confirm_attendance.html', {'form': form, 'event': event})

def event_attendees(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    attendees = EventsAttendee.objects.filter(event=event)

    return render(request, 'confirmed_attendees.html', {
        'event': event,
        'attendees': attendees,
    })

def edit_attendee(request, pk):
    attendee = get_object_or_404(EventsAttendee, pk=pk)
    if request.method == 'POST':
        form = EventsAttendeeForm(request.POST, instance=attendee)
        if form.is_valid():
            form.save()
            return redirect('events:attendees')  # Redirect to the attendees list after saving
    else:
        form = EventsAttendeeForm(instance=attendee)
    return render(request, 'edit_attendee.html', {'form': form, 'attendee': attendee})