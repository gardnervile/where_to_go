from django.contrib import admin

from .models import Place, PlaceImage

class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    fields = ['image', 'position']
    ordering = ['position']

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', "title", "latitude", "longitude")
    inlines = [PlaceImageInline]

@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'position']
    ordering = ['place', 'position']