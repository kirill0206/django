from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.
from mainapp.models import Product, ProductCategory


def main(request):
    return render(request, 'mainapp/index.html', context={'name': request.user, 'items': ['item1', 'item2', 'item3']})


def products(request, pk=None):
    print(pk)

    title = 'продукты'
    links_menu = ProductCategory.objects.all()
    basket = {}
    if not request.user.is_anonymous:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            category = {'name': 'все'}
            products = Product.objects.all().order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        context = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/product_list.html', context)

    hot_product = get_hot_product_from_admin()
    same_products = get_same_products(hot_product)

    context = {
        'title': title,
        'links_menu': links_menu,
        'hot_product': hot_product,
        'same_products': same_products,
        'basket': basket,
    }

    return render(request, 'mainapp/products.html', context)


def product(request, pk):
    title = 'продукты'

    content = {
        'title': title,
        'links_menu': ProductCategory.objects.all(),
        'product': get_object_or_404(Product, pk=pk),
    }

    return render(request, 'mainapp/products.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')


def media(request):
    return render(request, '../media')


