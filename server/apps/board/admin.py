from django.contrib import admin

from mptt.admin import MPTTModelAdmin

from apps.board.models import Category, ExpirationFilter, FilterAdvert, Advert


@admin.register(Category)
class CategoryAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = ("id", "name", "slug", "parent", "created", "updated")
    list_display_links = ("id", "name", "slug")
    list_filter = ("created", "updated")
    list_select_related = ("parent", )
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created", "updated")


@admin.register(FilterAdvert)
class FilterAdvertAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created", "updated")
    list_display_links = ("id", "name", "slug")
    list_filter = ("created", "updated")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created", "updated")


@admin.register(ExpirationFilter)
class ExpirationFilterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug", "created", "updated")
    list_display_links = ("id", "name", "slug")
    list_filter = ("created", "updated")
    search_fields = ("name", "slug")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("created", "updated")


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = (
        "id", "slug", "subject", "user", "category", "filter", "exp_filter", "price",
        "moderation", "created", "updated"
    )
    list_display_links = ("id", "slug", "subject")
    list_filter = ("category", "moderation", "filter", "exp_filter", "created", "updated")
    list_select_related = ("user", "category", "filter", "exp_filter", "image")
    search_fields = ("slug", "subject", "user__email")
    prepopulated_fields = {"slug": ("user", "subject")}
    readonly_fields = ("created", "updated")
