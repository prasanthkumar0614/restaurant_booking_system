from django.conf import settings
from django.db import models
from bookings.models import Booking
from menu.models import MenuItem


class Order(models.Model):
    STATUS_CHOICES = [
        ('placed', 'Placed'),
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
        ('completed', 'Completed'),
    ]
    ORDER_TYPE_CHOICES = [
        ('dine_in', 'Dine-in'),
        ('takeaway', 'Takeaway'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders')
    booking = models.ForeignKey(Booking, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE_CHOICES, default='dine_in')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='placed')
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())

    def __str__(self):
        return f"Order #{self.id} - {self.customer.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @property
    def subtotal(self):
        return self.menu_item.price * self.quantity

    def __str__(self):
        return f"{self.quantity} x {self.menu_item.name}"