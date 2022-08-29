from rest_framework import viewsets
from cost.serializers import ShopDaySerializer
from cost.models import ShopDay
from cost import filters
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class ShopDayViewSet(viewsets.ModelViewSet):
    queryset = ShopDay.objects.all()
    serializer_class = ShopDaySerializer
    filterset_class = filters.ShopDayFilter
    filter_backends = (OrderingFilter, DjangoFilterBackend )
    ordering_fields = ('shop_date',)
