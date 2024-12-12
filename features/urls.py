
# features/urls.py
from django.urls import path
from . import views

app_name = 'features'

urlpatterns = [
    path('feature/', views.feature_view, name='feature'),
]
