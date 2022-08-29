from django.db import models


class ShopDay(models.Model):
    shop_id = models.CharField(max_length=15, null=True, blank=True)
    shop_name = models.CharField(max_length=255, null=True, blank=True)
    simple_name = models.CharField(max_length=255, null=True, blank=True, verbose_name='商品简称')
    shop_date = models.DateField(null=True, blank=True)
    sales = models.FloatField(max_length=11, null=True, blank=True)
    train_cost = models.FloatField(null=True, blank=True)
    tuijian_cost = models.FloatField(null=True, blank=True)

