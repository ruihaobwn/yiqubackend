from rest_framework import serializers
from cost.models import ShopDay


class ShopDaySerializer(serializers.ModelSerializer):
    # shop_id = serializers.IntegerField()
    # shop_date = serializers.DateField()
    # shop_name = serializers.CharField()
    # sales = serializers.CharField()
    # train_cost = serializers.FloatField()
    # tuijian_cost = serializers.FloatField()

    class Meta:
        model = ShopDay
        fields = ['shop_id', 'shop_date', 'shop_name', 'simple_name', 'sales', 'train_cost', 'tuijian_cost']
