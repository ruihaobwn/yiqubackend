# Generated by Django 4.1 on 2022-08-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0008_alter_shopday_sales'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopday',
            name='simple_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='商品简称'),
        ),
    ]