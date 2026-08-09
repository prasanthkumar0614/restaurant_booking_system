from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_booking, name='create_booking'),
    path('mine/', views.my_bookings, name='my_bookings'),
    path('<int:booking_id>/food-prompt/', views.food_prompt, name='food_prompt'),
    path('<int:booking_id>/cancel/', views.cancel_booking, name='cancel_booking'),
    path('availability/', views.check_availability, name='check_availability'),
]