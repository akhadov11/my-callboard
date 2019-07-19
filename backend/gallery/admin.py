from django.contrib import admin

from .models import Gallery, Photo


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on", "id")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name", "created_on")
    search_fields = ("name", "created_on")


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("name", "created_on", "id")
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("name", "created_on")
    search_fields = ("name", "created_on")
