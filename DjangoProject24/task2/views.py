from django.shortcuts import render
from django.http import HttpResponse
import random
import logging

logger = logging.getLogger(__name__)


def index(request):
    return HttpResponse("Hello world")


def about(request):
    return HttpResponse("About me")


def heads_or_tails(request):
    list_of_choice = ["Heads", "Tails"]
    result = random.choice(list_of_choice)
    logger.info(f"The choice is {result}")
    return HttpResponse(f"{result}")


def random_number_cube(request):
    result_cube = random.randint(1, 6)
    logger.info(f"The cube side is {result_cube}")
    return HttpResponse(f'random number: {result_cube}')


def random_number_hundred(request):
    result_num = random.randint(1, 100)
    logger.info(f"The random number is {result_num}")
    return HttpResponse(f'random number: {result_num}')
