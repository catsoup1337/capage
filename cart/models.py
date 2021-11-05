from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


User = get_user_model()
# Create your models here.


# class Customer(models.Model):
#     user = models.ForeignKey(
#         User,
#         verbose_name="Пользователь",
#         on_delete=models.CASCADE)
#     phone = models.CharField(
#         max_length=20,
#         verbose_name="Номер телефона",
#         null=True,
#         blank=True)
#     email = models.CharField(
#         max_length=100,
#         verbose_name="Почта",
#         null=True,
#         blank=True)
#     adress = models.CharField(
#         max_length=255,
#         verbose_name="Адрес",
#         null=True,
#         blank=True)
#     orders = models.ManyToManyField(
#         "Order",
#         verbose_name="Заказы покупателя",
#         related_name="related_customer",
#         null=True,
#         blank=True)

#     def __str__(self):
#         return "Покупатель {}{}".format(
#             self.user.first_name, self.user.last_name)


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    orders = models.ManyToManyField(
        "Order",
        verbose_name="Заказы покупателя",
        related_name="orders",
        null=True,
        blank=True)

@receiver(post_save, sender=User)
def create_user_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_account(sender, instance, **kwargs):
    instance.account.save()

class Order(models.Model):
    STATUS_NEW = 'new'
    STATUS_IN_PROGRESS = 'in_progress'
    STATUS_READY = 'is_ready'
    STATUS_COMPLETED = 'completed'

    BYING_TYPE_SELF = 'self'
    BYING_TYPE_DELIVERY = 'delivery'

    STATUS_CHOICES = (
        (STATUS_NEW, "Новый заказ"),
        (STATUS_IN_PROGRESS, "Заказ в обработке"),
        (STATUS_READY, "Заказ готов"),
        (STATUS_COMPLETED, "Заказ выполнен"),
    )

    BYING_TYPE_CHOICES = (
        (BYING_TYPE_DELIVERY, "Доставка"),
        (BYING_TYPE_SELF, "Самовывоз"),
    )

    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        verbose_name="Покупатель",
        related_name="orders",
        on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия")
    email = models.EmailField(max_length=100, verbose_name="Email", null=True,blank=True)
    phone = models.CharField(max_length=15, verbose_name="Номер телефона")
    in_cart = models.TextField(
        max_length=2555, 
        verbose_name="Корзина",
        null=True,
        blank=True)
    # products_in_the_cart = models.CharField(max_length=400,null=True,blank=True)
    address = models.CharField(
        max_length=255,
        verbose_name="Адрес",
        null=True,
        blank=True)
    status = models.CharField(
        max_length=100,
        verbose_name="Статус заказа",
        choices=STATUS_CHOICES,
        default=STATUS_NEW
    )
    bying_type = models.CharField(
        max_length=100,
        verbose_name="Тип заказа",
        choices=BYING_TYPE_CHOICES,
        default=BYING_TYPE_SELF
    )
    comment = models.TextField(
        verbose_name="Комментарий к заказу",
        null=True,
        blank=True)
    created_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата создания заказа")
    order_date = models.DateField(
        verbose_name="Дата получения заказа",
        default=timezone.now)

    def __str__(self):
        return str(self.id)
