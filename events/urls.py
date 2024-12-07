from django.urls import path
from . import views

app_name = 'events'

urlpatterns =[
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),

    path('event/<int:event_id>/register/', views.register_attendee, name='register_attendee'),

   path('attendees/', views.attendee_list, name='attendees'),
]
