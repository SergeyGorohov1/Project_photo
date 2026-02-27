from django.contrib import admin
from django.utils.html import mark_safe
from gallery.models import Photo
from easy_thumbnails.files import get_thumbnailer
from adminsortable2.admin import SortableAdminMixin

@admin.register(Photo)
class PhotoAdmin(SortableAdminMixin, admin.ModelAdmin):
    pass
    list_display = ["preview", "name"]

    def preview(self, obj):
        thumbnailer = get_thumbnailer(obj.image)
        options = {'size': (40, 40), 'crop': True, 'upscale': True}
        thumbnail = thumbnailer.get_thumbnail(options)
        return mark_safe(f'<img src="{thumbnail.url}" />')

    def name(self, obj):
        return obj.image

    name.short_description = 'Название'
    preview.short_description = "Превью"
