from django.urls import path

from .views import *

urlpatterns = [
    path("", AdvertListView.as_view(), name='advert-list'),
    path("create/", AdvertCreateView.as_view()),
    path("adverts/", UserAdvertListView.as_view()),
    path("update-advert/<int:pk>/", UserAdvertUpdateView.as_view()),
    path("delete-advert/<int:pk>/", UserAdvertDeleteView.as_view()),
    path("<slug:slug>/", AdvertDetailView.as_view(), name='advert-detail'),
]
