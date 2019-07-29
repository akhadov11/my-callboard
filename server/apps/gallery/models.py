from django.db import models

from apps.core.utils.files import UniqueUploadPath


gallery_images_upload = UniqueUploadPath('gallery/images')


class Photo(models.Model):
    name = models.CharField(max_length=55, unique=True)
    image = models.ImageField("Photo", upload_to=gallery_images_upload)
    slug = models.SlugField(max_length=55, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Gallery(models.Model):
    name = models.CharField(max_length=55, unique=True)
    slug = models.SlugField(max_length=55, unique=True)
    photos = models.ManyToManyField(Photo, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
