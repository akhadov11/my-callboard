from django.contrib.auth import get_user_model
from rest_framework import serializers

# from backend.gallery.serializers import GallerySerializer
from .models import *

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email")
        # extra_kwargs = {"password":
        #                     {"write_only": True}
        #                 }

    # def create(self, validated_data):
    #     username = validated_data["username"]
    #     password = validated_data["password"]
    #     email = validated_data["email"]
    #     user_obj = User(
    #         username=username,
    #         email=email
    #     )
    #     user_obj.set_password(password)
    #     user_obj.save()
    #     return validated_data


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ("user", "avatar", "second_email", "phone", "fname", "lname")


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar", "second_email", "phone", "fname", "lname")


class AvatarUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("avatar",)
