from django.contrib.auth.views import LogoutView
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


app_name = 'Members'
urlpatterns = [
    path('', views.index, name='index'),

    path('login/', views.login_view, name='login'),

    path('update/<int:pk>/', views.member_update, name='member_update'),

    path('register/', views.register, name='register'),

    path('member_list/', views.member_list, name='member_list'),  # List of members

    path('detail/<int:pk>/', views.member_detail, name='member_detail'),

    path('logout/', LogoutView.as_view(), name='logout'),

    path('password-reset/', views.password_reset, name='password_reset'),

    path('password-reset/confirm/', views.password_reset_confirm, name='password_reset_confirm'),

    path('password-reset/success/', views.password_reset_success, name='password_reset_success'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
