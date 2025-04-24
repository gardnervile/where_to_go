import traceback
import sys

from django.contrib import admin
from django.utils.html import format_html
from adminsortable2.admin import SortableAdminBase, SortableInlineAdminMixin

from .models import Place, PlaceImage


class PlaceImageInline(SortableInlineAdminMixin, admin.TabularInline):
    model = PlaceImage
    extra = 1
    readonly_fields = ['get_preview']
    fields = ['image', 'get_preview']
    ordering = ['position']

    def get_preview(self, obj):
        try:
            if obj.image:
                return format_html('<img src="{}" style="max-height: 200px;" />', obj.image.url)
        except Exception as e:
            print('Ошибка в get_preview Inline:', e)
            traceback.print_exc(file=sys.stdout)
        return "—"

    get_preview.short_description = "Превью"

@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ('id', "title", "latitude", "longitude")
    inlines = [PlaceImageInline]


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ['place', 'position']
    ordering = ['place', 'position']