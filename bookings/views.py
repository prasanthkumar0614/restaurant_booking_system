from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking, Table


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            table = form.cleaned_data['table']
            date = form.cleaned_data['date']
            time_slot = form.cleaned_data['time_slot']

            requested_dt = datetime.combine(date, time_slot)
            window_start = requested_dt - timedelta(hours=4)
            window_end = requested_dt + timedelta(hours=4)

            conflicting_end_times = []
            existing_bookings = Booking.objects.filter(table=table, date=date).exclude(status='cancelled')
            for existing in existing_bookings:
                existing_dt = datetime.combine(existing.date, existing.time_slot)
                if window_start <= existing_dt <= window_end:
                    conflicting_end_times.append(existing_dt + timedelta(hours=4))

            if conflicting_end_times:
                free_from = max(conflicting_end_times)
                messages.error(
                    request,
                    "Table " + str(table.table_number) + " is already booked around that time. "
                    "It will be free from " + free_from.strftime('%I:%M %p') + " onwards on " + str(free_from.date()) + "."
                )
            else:
                booking = form.save(commit=False)
                booking.customer = request.user
                booking.status = 'confirmed'
                booking.save()
                messages.success(request, "Your table is booked! Pay the ₹100 advance below to confirm it.")
                return redirect('food_prompt', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def food_prompt(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    return render(request, 'bookings/food_prompt.html', {'booking': booking})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer=request.user)
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, customer=request.user)
    if request.method == 'POST':
        booking.status = 'cancelled'
        booking.save()
        messages.success(request, "Your booking has been cancelled.")
    return redirect('order_history')


def check_availability(request):
    tables = Table.objects.all()
    date_str = request.GET.get('date')
    selected_date = None
    availability = []

    if date_str:
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
        for table in tables:
            bookings_today = Booking.objects.filter(table=table, date=selected_date).exclude(status='cancelled')
            booked_times = [b.time_slot.strftime('%I:%M %p') for b in bookings_today]
            availability.append({
                'table': table,
                'booked_times': booked_times,
                'is_free_now': len(booked_times) == 0,
            })

    return render(request, 'bookings/availability.html', {
        'availability': availability,
        'selected_date': selected_date,
    })