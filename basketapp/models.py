from django.db import models
from django.conf import settings
from mainapp.models import Product

class Basket(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='basket')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)
    created = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='время последнего изменения', auto_now=True)
