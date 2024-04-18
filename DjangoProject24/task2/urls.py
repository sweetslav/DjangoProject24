"""
URL configuration for DjangoProject24 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from .views import index, about, heads_or_tails, random_number_cube, random_number_hundred

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('coin/', heads_or_tails, name='coin'),
    path('cube/', random_number_cube, name='cube'),
    path('hundred/', random_number_hundred, name='hundred'),
]
