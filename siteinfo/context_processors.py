from .models import RestaurantProfile


def restaurant_profile(request):
    profile = RestaurantProfile.objects.first()
    return {'restaurant_profile': profile}