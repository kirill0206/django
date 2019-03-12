from django.shortcuts import render
from .models import ProductCategory, Product

# Create your views here.
from mainapp.models import Product


def main(request):
    return render(request, 'mainapp/index.html', context={'name': request.user, 'items': ['item1', 'item2', 'item3']})


def catalog(request):
    return render(request, 'mainapp/catalog.html', context={'products': Product.objects.all()})


def contact(request):
    return render(request, 'mainapp/contact.html')


def media(request):
    return render(request, '../media')


