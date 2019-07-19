from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Category, ExpirationFilter, FilterAdvert, Advert


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    list_display = ("name", "parent", "id")
    mptt_level_indent = 20
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "parent")


@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", )


@admin.register(ExpirationFilter)
class ExpirationFilterAdmin(admin.ModelAdmin):
    list_display = ("name", "id")
    list_display_links = ("name",)
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", )


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ("id", "subject", "user", "category", "filter", "exp_filter", "price", "created_on", "moderation")
    list_display_links = ("subject",)
    list_filter = ("user", "category", "filter", "exp_filter", "price")
    prepopulated_fields = {"slug": ("user", "subject")}
    search_fields = ("subject", "user", "category", "exp_filter", "created_on",)
