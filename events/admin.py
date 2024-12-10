from django.contrib import admin


from .models import Event, EventsAttendee

admin.site.register(Event)
admin.site.register(EventsAttendee)
