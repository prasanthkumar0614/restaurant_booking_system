from django.urls import path
from . import views

urlpatterns = [
    path('', views.restaurant_info, name='restaurant_info'),
]