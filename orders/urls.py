from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('history/', views.order_history, name='order_history'),
]
