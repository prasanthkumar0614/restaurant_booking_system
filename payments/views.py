import random
import string

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from bookings.models import Booking
from orders.models import Order
from .models import Payment


def _generate_txn_id():
    return 'TXN' + ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))


@login_required
def pay_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    amount = 100 

    if request.method == 'POST':
        payment = Payment.objects.create(
            customer=request.user,
            booking=booking,
            amount=amount,
            method='card',
            status='success',
            transaction_id=_generate_txn_id(),
        )
        booking.advance_paid = True
        booking.save()
        messages.success(request, "Payment of Rs " + str(amount) + " successful! Your table is fully confirmed.")
        return redirect('food_prompt', booking_id=booking.id)

    return render(request, 'payments/payment_form.html', {
        'amount': amount,
        'label': "Advance payment for " + str(booking.table) + " on " + str(booking.date),
        'post_url_name': 'pay_booking',
        'obj_id': booking.id,
    })


@login_required
def pay_order(request, order_id):
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    amount = order.total_price

    if request.method == 'POST':
        payment = Payment.objects.create(
            customer=request.user,
            order=order,
            amount=amount,
            method='card',
            status='success',
            transaction_id=_generate_txn_id(),
        )
        order.is_paid = True
        order.save()
        messages.success(request, "Payment of Rs " + str(amount) + " successful! Your food order is confirmed.")
        return redirect('order_history')

    return render(request, 'payments/payment_form.html', {
        'amount': amount,
        'label': "Payment for Order #" + str(order.id),
        'post_url_name': 'pay_order',
        'obj_id': order.id,
    })