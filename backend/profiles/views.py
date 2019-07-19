from rest_framework import generics, permissions

from .models import Profile
from .serializers import ProfileSerializer, ProfileUpdateSerializer, AvatarUpdateSerializer


# class ProfileCreateView(generics.CreateAPIView):
#     serializer_class = ProfileSerializer
#     queryset = Profile.objects.all()
#

class ProfileDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class ProfileUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = ProfileUpdateSerializer


class ProfileAvatarUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Profile.objects.all()
    serializer_class = AvatarUpdateSerializer
