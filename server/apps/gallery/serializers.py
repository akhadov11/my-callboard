from rest_framework import serializers

from apps.gallery.models import Photo, Gallery


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ("image",)


class GallerySerializer(serializers.ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = ("photos", )
