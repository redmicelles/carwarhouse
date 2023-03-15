from django.contrib import admin
from django.utils.html import format_html
from .models import Car
from typing import Any

# Register your models here.

class CarAdmin(admin.ModelAdmin):
    def thumbnail(self, object) -> Any:
        """this method displays the thumbnails of cars"""
        return format_html('<img src="{}" width="40" style="border-radius: 10px;"/>'.format(object.car_photo.url))
    
    thumbnail.short_description = 'Thumbnail' #this attribute renames the thumbnail column to PHOTO
    list_display: tuple = ('id', 'thumbnail', 'car_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'is_featured', 'condition', 'price')
    list_display_links: tuple = ('id', 'thumbnail', 'car_title')
    list_editable: tuple = ('is_featured',)
    search_fields: tuple = ('id', 'car_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter: tuple = ('city', 'model', 'body_style', 'fuel_type')
admin.site.register(Car, CarAdmin)
