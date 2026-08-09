from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from bookings.models import Booking
from .forms import ReviewForm
from .models import Category, MenuItem, Review


def menu_list(request):
    categories = Category.objects.prefetch_related('items').all()

    booking = None
    booking_id = request.GET.get('booking')
    if booking_id and request.user.is_authenticated:
        booking = Booking.objects.filter(id=booking_id, customer=request.user).first()

    return render(request, 'menu/menu_list.html', {
        'categories': categories,
        'booking': booking,
    })


def reviews_list(request):
    reviews = Review.objects.select_related('menu_item', 'customer').all()

    if request.method == 'POST' and request.user.is_authenticated:
        form = ReviewForm(request.POST)
        if form.is_valid():
            Review.objects.create(
                menu_item=form.cleaned_data['menu_item'],
                customer=request.user,
                rating=form.cleaned_data['rating'],
                comment=form.cleaned_data['comment'],
            )
            messages.success(request, "Thanks for your review!")
            return redirect('reviews_list')
    else:
        form = ReviewForm()

    return render(request, 'menu/reviews_list.html', {
        'reviews': reviews,
        'form': form,
        'menu_items': MenuItem.objects.all(),
    })