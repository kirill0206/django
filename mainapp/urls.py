from django.conf.urls import url
from .views import products, product

app_name = 'mainapp'

urlpatterns = [
    url(r'^$', products, name='index'),
    url(r'^(?P<pk>\d+)/$', product, name='product'),
    url(r'^category/(?P<pk>\d+)/$', products, name='category')
]