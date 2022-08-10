from rest_framework import generics
from .models import PoliceCalls

from .serializers import CallsSerializer
from .service import PaginationCalls, CallsFilter
from django_filters.rest_framework import DjangoFilterBackend


class CallsView(generics.ListAPIView):
    queryset = PoliceCalls.objects.all()
    serializer_class = CallsSerializer
    pagination_class = PaginationCalls
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CallsFilter
    filterset_fields = ('report_date')
