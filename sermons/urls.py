# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('features/', views.features_page, name='features_page'),
    path('prayer-requests/', views.prayer_request_view, name='prayer_requests'),
    path('sermons/', views.sermons, name='sermons'),
    path('devotions/', views.devotions, name='devotions'),
    path('thank-you/', views.thank_you, name='thank_you'),
]
