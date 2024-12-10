from django.urls import path
from . import views
from .views import no_permission

urlpatterns = [
    path('send-newsletter/', views.send_newsletter, name='send_newsletter'),
    path('newsletter-sent/', views.newsletter_sent, name='newsletter_sent'),

    path('no_permission/', views.no_permission, name='no_permission'),
]
