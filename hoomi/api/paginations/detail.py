from rest_framework.pagination import PageNumberPagination


class DetailPagination(PageNumberPagination):
    page_size = 1
