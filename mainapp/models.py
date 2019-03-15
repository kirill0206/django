from django.db import models

# Create your models here.


class ProductCategory(models.Model):
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории продуктов"

    name = models.CharField(verbose_name='имя категории ', max_length=255, unique=True)
    description = models.TextField(verbose_name='имя категории', max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='имя продукта', max_length=128)
    image = models.ImageField(upload_to='products_images', blank=True, default='default/product.jpg')
    short_desc = models.CharField(verbose_name='краткое описание продукта', max_length=60, blank=True)
    description = models.TextField(verbose_name='описание продукта', blank=True)
    price = models.DecimalField(verbose_name='цена продукта', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество на складе', default=0)
    is_hot = models.BooleanField(verbose_name='является горячим продуктом?', default=False)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

