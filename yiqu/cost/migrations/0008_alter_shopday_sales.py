# Generated by Django 4.1 on 2022-08-28 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cost', '0007_alter_shopday_train_cost_alter_shopday_tuijian_cost'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopday',
            name='sales',
            field=models.FloatField(blank=True, max_length=11, null=True),
        ),
    ]