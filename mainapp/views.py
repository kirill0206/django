from django.shortcuts import render

# Create your views here.


def main(request):
	return render(request, 'mainapp/index.html')


def catalog(request):
	return render(request, 'mainapp/catalog.html')


def contact(request):
	return render(request, 'mainapp/contact.html')
