
# features/urls.py
from django.urls import path
from . import views

app_name = 'features'  # Set the correct app_name

urlpatterns = [
    path('feature/', views.feature_view, name='feature'),
]
