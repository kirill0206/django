from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.


def main(request):
    title = 'главная'

    products = Product.objects.all()[:4]

    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    return render(request, 'mainapp/catalog.html')


def contact(request):
    return render(request, 'mainapp/contact.html')


def media(request):
    return render(request, '../media')


