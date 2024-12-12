
# models.py
from django.db import models

class Payment(models.Model):
    PAYMENT_TYPES = (
        ('donation', 'Donation'),
        ('tithe', 'Tithe'),
        ('offering', 'Offering'),
        ('other', 'Other'),
    )

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_type = models.CharField(choices=PAYMENT_TYPES, max_length=10)
    phone_number = models.CharField(max_length=15)
    name = models.CharField(max_length=100,default='kaguru stanley')  # Add name field
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.payment_type} - {self.amount} from {self.phone_number}"
