from django.urls import path
from . import views
from .views import contact_view, thank_you_view

app_name = 'blog'
urlpatterns=[

    path('testimonials/',views.testimonials,name='testimonials'),
    path('pricing/',views.pricing,name='pricing'),

    path('contact/', contact_view, name='contact'),
    path('thank-you/', thank_you_view, name='thank_you'),

]

