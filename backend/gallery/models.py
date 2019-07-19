import os
from datetime import datetime

from PIL import Image
from django.db import models
from django.utils import timezone


def get_path_upload_image(file):
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[-1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + timezone.now().strftime("%H-%M-%S") + '.' + end_extention
    return os.path.join('photos', f'{time}', f'{file_name}')


class Photo(models.Model):
    name = models.CharField(max_length=55, unique=True)
    image = models.ImageField("Photo", upload_to="gallery/")
    created_on = models.DateTimeField("Creation date", auto_now_add=True)
    slug = models.SlugField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image.name = get_path_upload_image(self.image.name)
        super().save(*args, **kwargs)
        #
        # if self.image:
        #     img = Image.open(self.image.path)
        #     if img.height > 200 and img.width > 200:
        #         output_size = (200, 200)
        #         img.thumbnail(output_size)
        #         img.save(self.image.path)

    class Meta:
        verbose_name = "Photo"
        verbose_name_plural = "Photos"


class Gallery(models.Model):
    name = models.CharField(max_length=55, unique=True)
    photos = models.ManyToManyField(Photo, verbose_name="Photographs")
    created_on = models.DateTimeField("Creation date", auto_now_add=True)
    slug = models.SlugField(max_length=55, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Gallery"
        verbose_name_plural = "Galleries"
