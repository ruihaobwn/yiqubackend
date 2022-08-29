
from django_filters import rest_framework as filters

from cost.models import ShopDay


class ShopDayFilter(filters.FilterSet):
    shop_id = filters.CharFilter(lookup_expr='exact')
    shop_name = filters.CharFilter(lookup_expr='icontains')
    simple_name = filters.CharFilter(lookup_expr='icontains')
    shop_date = filters.DateFilter()

    class Meta:
        model = ShopDay
        fields = ['shop_id', 'simple_name', 'shop_name']
