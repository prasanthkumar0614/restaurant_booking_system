from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'order_type', 'status', 'created_at']
    list_filter = ['status', 'order_type']
    inlines = [OrderItemInline]
