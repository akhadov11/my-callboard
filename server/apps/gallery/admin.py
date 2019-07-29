from django.contrib import admin
from django.db.models import Count

from apps.gallery.models import Gallery, Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "images_count", "created", "updated")
    list_display_links = ("id", "name", "slug")
    list_filter = ("created", "updated")
    filter_horizontal = ("photos", )
    search_fields = ("name", "slug")
    readonly_fields = ("created", "updated")
    prepopulated_fields = {"slug": ("name",)}

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(images_count=Count("photos"))

    @staticmethod
    def images_count(obj):
        return obj.images_count


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "image", "created", "updated")
    list_display_links = ("id", "name", "slug")
    list_filter = ("created", "updated")
    search_fields = ("name", "slug")
    readonly_fields = ("created", "updated")
    prepopulated_fields = {"slug": ("name",)}
