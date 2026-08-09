from django.contrib import admin
from .models import RestaurantProfile, RestaurantImage


@admin.register(RestaurantProfile)
class RestaurantProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact_number', 'email', 'opening_time', 'closing_time']


@admin.register(RestaurantImage)
class RestaurantImageAdmin(admin.ModelAdmin):
    list_display = ['caption', 'category', 'uploaded_at']
    list_filter = ['category']