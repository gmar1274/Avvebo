"""Avvebo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include,path,re_path
from django.contrib import admin
from Avvebo.website import urls as website_urls
from django.urls import path, re_path, include

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.core import urls as wagtail_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #re_path(r'', include(wagtail_urls)),
    #path('admin/', admin.site.urls), 
    
    re_path(r'',include(website_urls)),
    re_path(r'^cms/', include(wagtailadmin_urls)),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    re_path(r'^pages/', include(wagtail_urls)),
    
    #path('', route, {'template':'index.html','object_list':TalentContent.objects.all()}),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
