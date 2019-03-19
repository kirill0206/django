from django.contrib import admin
from .models import ShopUser
from mainapp.models import Product, ProductCategory
# Register your models here.

admin.site.register(ShopUser)
#admin.site.register(Product)
admin.site.register(ProductCategory)
