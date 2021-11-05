from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from cart.models import Order

class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(
        Order,
        verbose_name="Заказы покупателя",
        related_name="related_customer",
        null=True,
        blank=True)