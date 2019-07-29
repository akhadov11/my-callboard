from rest_framework import pagination


class AdvertPageNumberPagination(pagination.PageNumberPagination):
    page_size = 2
