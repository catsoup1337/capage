# Generated by Django 2.2.6 on 2021-10-11 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_remove_order_products_in_the_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='in_cart',
            field=models.CharField(blank=True, max_length=2555, null=True, verbose_name='Корзина'),
        ),
    ]
