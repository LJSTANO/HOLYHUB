from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db import models

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class EventAttendee(models.Model):
        event = models.ForeignKey(Event, related_name='attendees', on_delete=models.CASCADE)
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        name = models.CharField(max_length=100,default='john')
        phone = models.CharField(max_length=15,default='07********')
        email = models.EmailField(default='<holyhub@gmail.com>')

        def __str__(self):
            return f'{self.name} - {self.event.title}'
