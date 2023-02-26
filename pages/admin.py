from django.contrib import admin
from .models import Team
from django.utils.html import format_html
from typing import Any

class TeamAdmin(admin.ModelAdmin):

    def thumbnail(self, object) -> Any:
        """this method displays the thumbnails of team members"""
        return format_html('<img src="{}" width="40" style="border-radius: 50%;"/>'.format(object.photo.url))
    
    thumbnail.short_description = 'Photo' #this attribute renames the thumbnail column to PHOTO
    
    list_display: tuple = ('id', 'thumbnail', 'first_name', 'last_name', 'designation', 'created_date')
    list_display_links: tuple = ('id', 'thumbnail')
    search_fields: tuple = ('first_name', 'last_name', 'designation')
    list_filter: tuple  = ('designation',)
    list_editable: tuple = ('designation',)

# Register your models here.
admin.site.register(Team, TeamAdmin)
