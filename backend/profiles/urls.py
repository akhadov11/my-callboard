from django.urls import path

from .views import *

urlpatterns = [
    path('<int:pk>/', ProfileDetailView.as_view()),
    path('update/<int:pk>/', ProfileUpdateView.as_view()),
    path('update/avatar/<int:pk>/', ProfileAvatarUpdateView.as_view()),
    # path('create/', ProfileCreateView.as_view())
]
