from django.urls import path
from . import views

app_name = 'events'

urlpatterns =[
    path('', views.event_list, name='event_list'),
    path('create/', views.event_create, name='event_create'),
    path('attendees/', views.attendees_list, name='attendees'),
    path('attendees/confirm/<int:event_id>/', views.confirm_attendance, name='confirm_attendance'),

    path('attendee/edit/<int:pk>/', views.edit_attendee, name='edit_attendee'),

    path('event/<int:event_id>/attendees/', views.event_attendees, name='event_attendees'),

    path('attendee/edit/<int:pk>/', views.edit_attendee, name='edit_attendee'),
]