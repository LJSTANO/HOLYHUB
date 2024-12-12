from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import requests
from .models import Payment
from .mpesa import AccessToken, Password, Credentials
from django.views.decorators.csrf import csrf_exempt
import json
from django.db.models import Sum
from django.contrib.auth.decorators import login_required


def stk_push(request):
    if request.method == 'POST':
        # Get the phone number and amount from the form submission
        phone = request.POST.get('phone_number')  # Ensure you are getting the correct field
        amount = request.POST.get('amount')

        # Check if the phone number starts with '254' and has exactly 13 digits
        if not phone.startswith("254") or len(phone) != 12 or not phone.isdigit():
            return HttpResponse("Invalid phone number. It must start with 254 and contain 13 digits.", status=400)

        # Get access token
        access_token = AccessToken.get_access_token()
        if not access_token:
            return HttpResponse("Failed to get access token", status=400)

        # API URL for MPesa STK Push
        api_url = 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest'

        # Get the password and timestamp from the Password class
        password, timestamp = Password.generate_password()

        # Prepare the request payload
        request_data = {
            "BusinessShortCode": Credentials.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,  # Ensure the phone number is correctly passed here
            "PartyB": Credentials.shortcode,
            "PhoneNumber": phone,  # Ensure the phone number is correctly passed here
            "CallBackURL": "https://5c53-102-217-64-115.ngrok-free.app/mpesa/callback/",  # Update with your ngrok URL
            "AccountReference": "HolyHub",
            "TransactionDesc": "Donation/Tithe/Offering"
        }

        # Request headers
        headers = {
            "Authorization": f"Bearer {access_token}"
        }

        # Send the request to MPesa
        response = requests.post(api_url, json=request_data, headers=headers)

        if response.status_code == 200:
            return HttpResponse("Payment initiated successfully", status=200)
        else:
            return HttpResponse(f"Failed to initiate payment. Response: {response.text}", status=400)

    return render(request, 'payment_form.html')

def mpesa_callback(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        callback_data = json.loads(request.body)

        # Print the response for debugging
        print(callback_data)

        # Check if the response contains 'Body' and 'stkCallback'
        if 'Body' in callback_data and 'stkCallback' in callback_data['Body']:
            callback = callback_data['Body']['stkCallback']

            # Get the relevant data from the response
            result_code = callback.get('ResultCode')
            result_desc = callback.get('ResultDesc')

            if result_code == 0:
                # Payment was successful
                # Store the payment information in the database
                phone = callback['CallbackMetadata']['Item'][4]['Value']  # Phone number from the callback
                amount = callback['CallbackMetadata']['Item'][0]['Value']  # Amount from the callback
                payment_type = 'donation'  # Assuming donation, you can adjust this
                payment = Payment.objects.create(
                    amount=amount,
                    payment_type=payment_type,
                    phone_number=phone,
                    status='Completed'
                )
                payment.save()
                return JsonResponse({"message": "Payment successfully recorded."}, status=200)
            else:
                # Payment failed
                return JsonResponse({"message": f"Payment failed: {result_desc}"}, status=400)

    return JsonResponse({"message": "Invalid request"}, status=400)

def payment_form(request):
    return render(request, 'payment_form.html')


def finance_management(request):
    # Fetch payments for the logged-in user
    payments = Payment.objects.all().order_by('-date')
        # Assuming user field exists on Payment model

    # Summarize payment data (donations, tithes, offerings, etc.)
    total_donations = payments.filter(payment_type='donation').aggregate(Sum('amount'))['amount__sum'] or 0
    total_tithes = payments.filter(payment_type='tithe').aggregate(Sum('amount'))['amount__sum'] or 0
    total_offerings = payments.filter(payment_type='offering').aggregate(Sum('amount'))['amount__sum'] or 0
    total_other = payments.filter(payment_type='other').aggregate(Sum('amount'))['amount__sum'] or 0

    context = {
        'payments': payments,
        'total_donations': total_donations,
        'total_tithes': total_tithes,
        'total_offerings': total_offerings,
        'total_other': total_other,
    }

    return render(request, 'manage.html', context)

