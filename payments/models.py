from django.conf import settings
from django.db import models
from bookings.models import Booking
from orders.models import Order


class Payment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('success', 'Success'),
        ('failed', 'Failed'),
    ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    method = models.CharField(max_length=30, default='card')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=40, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Payment #" + str(self.id)