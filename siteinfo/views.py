from django.shortcuts import render
from .models import RestaurantProfile, RestaurantImage


def restaurant_info(request):
    profile = RestaurantProfile.objects.first()
    interior_images = RestaurantImage.objects.filter(category='interior')
    exterior_images = RestaurantImage.objects.filter(category='exterior')
    general_images = RestaurantImage.objects.filter(category='general')

    return render(request, 'restaurant_info.html', {
        'profile': profile,
        'interior_images': interior_images,
        'exterior_images': exterior_images,
        'general_images': general_images,
    })