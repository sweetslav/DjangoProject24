"""
URL configuration for config project.

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
from . import views

urlpatterns = [
    # Маршруты для фальшивых данных
    path('', views.shop_index, name='shop_index'),  # Маршрут для главной страницы магазина
    # path('create_fake_client/', views.create_fake_client, name='create_fake_client'),  # Маршрут для создания клиента
    # path('create_fake_product/', views.create_fake_product, name='create_fake_product'),  # Маршрут для создания товара
    # path('create_fake_order/', views.create_fake_order, name='create_fake_order'),  # Маршрут для создания заказа
    # path('write_fake_orders/', views.write_fake_orders, name='write_fake_orders'),  # Маршрут для записи готовых заказов
    #
    # # Маршруты для клиентов
    # path('clients/', views.client_list, name='client_list'),
    # path('clients/<int:client_id>/', views.client_detail, name='client_detail'),
    # path('clients/create/', views.create_client_view, name='create_client'),
    # path('clients/<int:client_id>/update/', views.update_client_view, name='update_client'),
    # path('clients/<int:client_id>/delete/', views.delete_client_view, name='delete_client'),
    #
    # # Маршруты для товаров
    # path('products/', views.product_list, name='product_list'),
    # path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    # path('products/create/', views.create_product_view, name='create_product'),
    # path('products/<int:product_id>/update/', views.update_product_view, name='update_product'),
    # path('products/<int:product_id>/delete/', views.delete_product_view, name='delete_product'),
    #
    # # Маршруты для заказов
    # path('orders/', views.order_list, name='order_list'),
    # path('orders/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('orders/create/', views.create_order_view, name='create_order'),
    # path('orders/<int:order_id>/update/', views.update_order_view, name='update_order'),
    # path('orders/<int:order_id>/delete/', views.delete_order_view, name='delete_order'),
]
