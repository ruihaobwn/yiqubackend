# Generated by Django 4.1 on 2022-08-25 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0004_alter_shopday_sales_alter_shopday_train_cost_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopday',
            name='shop_id',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
