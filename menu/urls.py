from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu_list, name='menu_list'),
    path('reviews/', views.reviews_list, name='reviews_list'),
]