from django.db.models import Q
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters


from backend.board.models import Advert
from backend.board.paginations import AdvertPageNumberPagination
from backend.board.permissions import IsOwnerOrReadOnly
from .serializers import AdvertListSerializer, AdvertDetailSerializer, AdvertCreateSerializer


class AdvertListView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = AdvertListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["subject", "category__name", "filter__name"]
    pagination_class = AdvertPageNumberPagination

    def get_queryset(self):
        queryset_list = Advert.objects.all()
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(subject__icontains=query) |
                    Q(category__name__icontains=query) |
                    Q(filter__name__icontains=query)
                ).distinct()
        return queryset_list


class AdvertDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Advert.objects.all()
    lookup_field = "slug"
    serializer_class = AdvertDetailSerializer


class AdvertCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Advert.objects.all()
    serializer_class = AdvertCreateSerializer

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class UserAdvertListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ["subject", "category__name", "filter__name"]

    def get_queryset(self):
        queryset_list = Advert.objects.filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(subject__icontains=query) |
                    Q(category__name__icontains=query) |
                    Q(filter__name__icontains=query)
                ).distinct()
        return queryset_list


class UserAdvertUpdateView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AdvertCreateSerializer

    def get_queryset(self):
        return Advert.objects.filter(user=self.request.user)


class UserAdvertDeleteView(generics.DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Advert.objects.filter(id=self.kwargs.get("pk"), user=self.request.user)
