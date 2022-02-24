# Generated by Django 3.2.8 on 2021-11-05 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_alter_order_user'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='orders',
        ),
        migrations.AddField(
            model_name='account',
            name='orders',
            field=models.ManyToManyField(blank=True, null=True, related_name='related_customer', to='cart.Order', verbose_name='Заказы покупателя'),
        ),
    ]