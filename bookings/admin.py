from django.contrib import admin
from .models import Table, Booking


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer', 'table', 'date', 'time_slot', 'guests', 'status']
    list_filter = ['status', 'date']
    search_fields = ['customer__username']
