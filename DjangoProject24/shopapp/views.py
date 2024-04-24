from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.http import HttpResponse
from django.utils import timezone
from .models import Client, Product, Order
import logging
import random
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()


def shop_index(request):
    return HttpResponse("<h1>This is shop index page</h1><br>")


# # Функция для создания нового клиента
# def create_client(name, email, phone, address):
#     client = Client.objects.create(
#         name=name,
#         email=email,
#         phone=phone,
#         address=address
#     )
#     return client
#
#
# # Функция для создания нового товара
# def create_product(name, description, price, quantity):
#     product = Product.objects.create(
#         name=name,
#         description=description,
#         price=price,
#         quantity=quantity
#     )
#     return product
#
#
# # Функция для создания нового заказа
# def create_order(client, products, total):
#     order = Order.objects.create(
#         client=client,
#         total=total
#     )
#     order.products.add(*products)
#     return order
#
#
# # Функция для получения всех клиентов
# def get_all_clients(request):
#     return Client.objects.all()
#
#
# # Функция для получения всех товаров
# def get_all_products(request):
#     return Product.objects.all()
#
#
# # Функция для получения всех заказов
# def get_all_orders(request):
#     return Order.objects.all()
#
#
# # Функция для получения клиента по ID
# def get_client_by_id(client_id):
#     return get_object_or_404(Client, pk=client_id)
#
#
# # Функция для получения товара по ID
# def get_product_by_id(product_id):
#     return get_object_or_404(Product, pk=product_id)
#
#
# # Функция для получения заказа по ID
# def get_order_by_id(order_id):
#     return get_object_or_404(Order, pk=order_id)
#
#
# # Функция для обновления информации о клиенте
# def update_client(client, name, email, phone, address):
#     client.name = name
#     client.email = email
#     client.phone = phone
#     client.address = address
#     client.save()
#     return client
#
#
# # Функция для обновления информации о товаре
# def update_product(product, name, description, price, quantity):
#     product.name = name
#     product.description = description
#     product.price = price
#     product.quantity = quantity
#     product.save()
#     return product
#
#
# # Функция для обновления информации о заказе
# def update_order(order, client, products, total):
#     order.client = client
#     order.total = total
#     order.products.clear()
#     order.products.add(*products)
#     order.save()
#     return order
#
#
# # Функция для удаления клиента
# def delete_client(client):
#     client.delete()
#
#
# # Функция для удаления товара
# def delete_product(product):
#     product.delete()
#
#
# # Функция для удаления заказа
# def delete_order(order):
#     order.delete()
#
#
# # Функция для отображения списка клиентов
# def client_list(request):
#     clients = get_all_clients()
#     return render(request, 'client_list.html', {'clients': clients})
#
#
# # Функция для отображения информации о клиенте
# def client_detail(request, client_id):
#     client = get_client_by_id(client_id)
#     return render(request, 'client_detail.html', {'client': client})
#
#
# # Функция для создания нового клиента
# def create_client_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         create_client(name, email, phone, address)
#         return HttpResponseRedirect(reverse('client_list'))
#     else:
#         return render(request, 'create_client.html')
#
#
# # Функция для обновления информации о клиенте
# def update_client_view(request, client_id):
#     client = get_client_by_id(client_id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         update_client(client, name, email, phone, address)
#         return HttpResponseRedirect(reverse('client_detail', args=[client_id]))
#     else:
#         return render(request, 'update_client.html', {'client': client})
#
#
# # Функция для удаления клиента
# def delete_client_view(request, client_id):
#     client = get_client_by_id(client_id)
#     delete_client(client)
#     return HttpResponseRedirect(reverse('client_list'))
#
#
# # Функция для отображения списка товаров
# def product_list(request):
#     products = get_all_products()
#     return render(request, 'product_list.html', {'products': products})
#
#
# # Функция для отображения информации о товаре
# def product_detail(request, product_id):
#     product = get_product_by_id(product_id)
#     return render(request, 'product_detail.html', {'product': product})
#
#
# # Функция для создания нового товара
# def create_product_view(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         create_product(name, description, price, quantity)
#         return HttpResponseRedirect(reverse('product_list'))
#     else:
#         return render(request, 'create_product.html')
#
#
# # Функция для обновления информации о товаре
# def update_product_view(request, product_id):
#     product = get_product_by_id(product_id)
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         description = request.POST.get('description')
#         price = request.POST.get('price')
#         quantity = request.POST.get('quantity')
#         update_product(product, name, description, price, quantity)
#         return HttpResponseRedirect(reverse('product_detail', args=[product_id]))
#     else:
#         return render(request, 'update_product.html', {'product': product})
#
#
# # Функция для удаления товара
# def delete_product_view(request, product_id):
#     product = get_product_by_id(product_id)
#     delete_product(product)
#     return HttpResponseRedirect(reverse('product_list'))
#
#
# # Функция для отображения списка заказов
# def order_list(request):
#     orders = get_all_orders()
#     return render(request, 'order_list.html', {'orders': orders})
#
#
# # Функция для отображения информации о заказе
# def order_detail(request, order_id):
#     order = get_order_by_id(order_id)
#     return render(request, 'order_detail.html', {'order': order})
#
#
# # Функция для создания нового заказа
# def create_order_view(request):
#     if request.method == 'POST':
#         client_id = request.POST.get('client_id')
#         product_ids = request.POST.getlist('product_ids')
#         total = request.POST.get('total')
#         client = get_client_by_id(client_id)
#         products = [get_product_by_id(product_id) for product_id in product_ids]
#         create_order(client, products, total)
#         return HttpResponseRedirect(reverse('order_list'))
#     else:
#         clients = get_all_clients()
#         products = get_all_products()
#         return render(request, 'create_order.html', {'clients': clients, 'products': products})
#
#
# # Функция для обновления информации о заказе
# def update_order_view(request, order_id):
#     order = get_order_by_id(order_id)
#     if request.method == 'POST':
#         client_id = request.POST.get('client_id')
#         product_ids = request.POST.getlist('product_ids')
#         total = request.POST.get('total')
#         client = get_client_by_id(client_id)
#         products = [get_product_by_id(product_id) for product_id in product_ids]
#         update_order(order, client, products, total)
#         return HttpResponseRedirect(reverse('order_detail', args=[order_id]))
#     else:
#         clients = get_all_clients()
#         products = get_all_products()
#         return render(request, 'update_order.html', {'order': order, 'clients': clients, 'products': products})
#
#
# # Функция для удаления заказа
# def delete_order_view(request, order_id):
#     order = get_order_by_id(order_id)
#     delete_order(order)
#     return HttpResponseRedirect(reverse('order_list'))
