from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DetailPagination(PageNumberPagination):
    page_size = 1
