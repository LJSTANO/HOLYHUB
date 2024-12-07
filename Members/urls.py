from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Members'
urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_view, name='login'),

    path('register/', views.register, name='register'),

    path('password_reset/', views.password_reset, name='password_reset'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
