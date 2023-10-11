"""
URL configuration for gblectproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from lect03app.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path('prefix/', include('lect01app.urls')),
    path('lect03/', include('lect03app.urls')),
    path('', index),    # базовый адрес всего сайта
    path('lect04/', include('lect04app.urls')),
    # path('lect05/', include('lect05app.urls')),
    # path('__debug__/', include('debug_toolbar.urls')),
    path('lect06/', include('lect06app.urls')),
]
