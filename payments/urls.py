from django.urls import path
from . import views

urlpatterns = [
    path('booking/<int:booking_id>/', views.pay_booking, name='pay_booking'),
    path('order/<int:order_id>/', views.pay_order, name='pay_order'),
]