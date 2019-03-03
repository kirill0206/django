"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  fr0om other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
import mainapp.views as mainapp

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', mainapp.main, name='main'),
    url(r'^catalog/', include('mainapp.urls', namespace='catalog'))
    url(r'^contact/', mainapp.contact, name='contact'),
    url(r'^admin/', admin.site.urls,  name='admin'),
    #path(r'^', mainapp.main, name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

