from django.conf import settings
from django.db import models


class Table(models.Model):
    table_number = models.PositiveIntegerField(unique=True)
    capacity = models.PositiveIntegerField(help_text="Max number of guests this table seats")

    def __str__(self):
        return f"Table {self.table_number} (seats {self.capacity})"


class Booking(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    booking_name = models.CharField(max_length=100, help_text="Name for this booking (e.g. the guest's name)")
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='bookings')
    date = models.DateField()
    time_slot = models.TimeField()
    guests = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    advance_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date', '-time_slot']

    def __str__(self):
        return f"{self.booking_name} - Table {self.table.table_number} on {self.date} at {self.time_slot}"