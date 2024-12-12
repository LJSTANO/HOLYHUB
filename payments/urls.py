from django.urls import path
from . import views

urlpatterns = [
    path('', views.stk_push, name='stkpush'),  # URL for handling the STK push payment
    path('mpesa/callback/', views.mpesa_callback, name='mpesa_callback'),

   path('payment-form/', views.payment_form, name='payment_form'),

    path('finance-management/', views.finance_management, name='finance_management'),
]
