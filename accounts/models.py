# from django.db import models
# from django.contrib.auth.models import User
# from django.conf import settings
# from cart.models import Order
# from django.db.models.signals import post_save
# from django.dispatch import receiver


# class Account(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     orders = models.ManyToManyField(
#         Order,
#         verbose_name="Заказы покупателя",
#         related_name="related_customer",
#         default = 1 , 
#         )

# @receiver(post_save, sender=User)
# def create_user_account(sender, instance, created, **kwargs):
#     if created:
#         Account.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_account(sender, instance, **kwargs):
#     instance.account.save()