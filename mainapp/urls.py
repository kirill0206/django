from django.conf.urls import url
from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   url('', mainapp.catalog, name='index'),
   path('<int:pk>/', mainapp.catalog, name='category'),
]