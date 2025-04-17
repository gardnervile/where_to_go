from django.contrib import admin

from .models import Place

@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("title", "latitude", "longitude")
# Register your models here.
