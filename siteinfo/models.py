from django.db import models


class RestaurantProfile(models.Model):
    name = models.CharField(max_length=150, default="Spice Route Restaurant")
    tagline = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=255, blank=True)
    contact_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(blank=True)
    opening_time = models.TimeField(null=True, blank=True)
    closing_time = models.TimeField(null=True, blank=True)
    logo = models.ImageField(upload_to='restaurant/', blank=True, null=True)
    banner_image = models.ImageField(upload_to='restaurant/', blank=True, null=True)

    def __str__(self):
        return self.name


class RestaurantImage(models.Model):
    CATEGORY_CHOICES = [
        ('interior', 'Interior'),
        ('exterior', 'Exterior'),
        ('general', 'General'),
    ]
    image = models.ImageField(upload_to='restaurant_gallery/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    caption = models.CharField(max_length=150, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category