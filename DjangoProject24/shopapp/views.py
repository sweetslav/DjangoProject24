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
