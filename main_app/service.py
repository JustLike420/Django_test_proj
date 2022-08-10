from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from .models import PoliceCalls


class PaginationCalls(PageNumberPagination):
    page_size = 20
    page_query_param = 'page'


class CallsFilter(filters.FilterSet):
    date = filters.DateTimeFromToRangeFilter(field_name='report_date')

    class Meta:
        model = PoliceCalls
        fields = ['report_date']
