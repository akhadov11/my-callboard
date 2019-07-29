from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from unidecode import unidecode
from mptt.models import MPTTModel, TreeForeignKey

from apps.core.utils.files import UniqueUploadPath

User = get_user_model()

advert_files_upload = UniqueUploadPath('board/advert/files')


class Category(MPTTModel):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    parent = TreeForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="children",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name_plural = "Categories"


class FilterAdvert(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Filter"
        verbose_name_plural = "Filters"


class ExpirationFilter(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "ExpFilter"
        verbose_name_plural = "ExpFilters"


class Advert(models.Model):
    slug = models.SlugField(max_length=255, unique=True)
    user = models.ForeignKey(User, verbose_name="User", on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name="Category", on_delete=models.CASCADE)
    filter = models.ForeignKey(FilterAdvert, verbose_name="Filter", on_delete=models.CASCADE)
    exp_filter = models.ForeignKey(
        ExpirationFilter, verbose_name="ExpFilter", on_delete=models.CASCADE
    )
    image = models.ForeignKey(
        'gallery.Gallery', verbose_name="Image", blank=True, null=True, on_delete=models.SET_NULL
    )
    subject = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)
    file = models.FileField(upload_to=advert_files_upload, blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    moderation = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = unidecode(self.subject) + "-" + str(self.user.id)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject

    def get_absolute_url(self):
        return reverse("advert-detail", kwargs={'category': self.category.slug, 'slug': self.slug})

    class Meta:
        verbose_name = "Advert"
        verbose_name_plural = "Adverts"
