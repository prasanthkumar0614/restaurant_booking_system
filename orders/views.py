from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from bookings.models import Booking
from menu.models import MenuItem
from .models import Order, OrderItem


@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    booking_id = request.GET.get('booking') or request.POST.get('booking')
    booking = None
    if booking_id:
        booking = get_object_or_404(Booking, id=booking_id, customer=request.user)

    if booking:
        order = Order.objects.filter(customer=request.user, booking=booking, status='placed').first()
    else:
        order = Order.objects.filter(customer=request.user, booking__isnull=True, status='placed').first()

    if not order:
        order = Order.objects.create(customer=request.user, booking=booking, status='placed')

    order_item, created = OrderItem.objects.get_or_create(order=order, menu_item=menu_item)
    if not created:
        order_item.quantity += 1
        order_item.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'success': True,
            'item_name': menu_item.name,
            'quantity': order_item.quantity,
        })

    if booking:
        return redirect(f"{reverse('menu_list')}?booking={booking.id}")
    return redirect('menu_list')


@login_required
def order_history(request):
    now = timezone.localtime().replace(tzinfo=None)

    all_bookings = Booking.objects.filter(customer=request.user).prefetch_related('orders__items')
    upcoming_bookings = [b for b in all_bookings if datetime.combine(b.date, b.time_slot) >= now]

    standalone_orders = Order.objects.filter(customer=request.user, booking__isnull=True).prefetch_related('items')
    return render(request, 'orders/order_history.html', {
        'bookings': upcoming_bookings,
        'standalone_orders': standalone_orders,
    })