from rest_framework import serializers

from apps.gallery.serializers import GallerySerializer
from apps.board.models import Category, FilterAdvert, Advert


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class FilterAdvertSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterAdvert
        fields = ("name",)


class AdvertListSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    filter = FilterAdvertSerializer()
    image = GallerySerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='advert-detail',
        lookup_field="slug"
    )

    class Meta:
        model = Advert
        fields = ("id", "url", "category", "filter", "subject", "image", "price", "created_on", "slug")


class AdvertDetailSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    filter = FilterAdvertSerializer()
    image = GallerySerializer(read_only=True)

    class Meta:
        model = Advert
        fields = ("category", "filter", "subject", "description", "image", "file", "price", "created_on", "user")


class AdvertCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advert
        fields = ("category", "filter", "exp_filter", "subject", "description", "price", "image")

    def create(self, request):
        request["user"] = self.context['request'].user
        advert = Advert.objects.create(**request)
        return advert
