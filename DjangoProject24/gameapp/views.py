from django.shortcuts import render
from django.http import HttpResponse
from .models import Coin
import random
import logging

logger = logging.getLogger(__name__)


def index(request):
    logger.info("Someone has visited the Index page ")
    return HttpResponse("<h1>This is index page</h1><br>"
                        "<h4>latine fames causae eu dui idque platonem iudicabit vehicula civibus</h4><br>"
                        "<h4>mi mus causae egestas pretium errem montes rutrum malesuada wisi</h4><br>")


def main(request):
    logger.info("Someone has visited the main page ")
    return HttpResponse("<h1>This is main page</h1><br>"
                        "<h4>latine fames causae eu dui idque platonem iudicabit vehicula civibus</h4><br>"
                        "<h4>mi mus causae egestas pretium errem montes rutrum malesuada wisi</h4><br>")


def about(request):
    logger.info("Someone has visited the 'about me' page ")
    return HttpResponse("<h1>This is About page</h1><br>"
                        "<h4>Name: Svyatoslav</h4><br>"
                        "<h4>Age: 29</h4><br>"
                        "<h4>City: Saint-Petersburg</h4><br>"
                        "<h4>Email: sweet@example.com</h4><br>")


def heads_or_tails(request):
    coin_side = random.choice(["Heads", "Tails"])
    coin = Coin(side=coin_side)
    coin.save()
    logger.info(f"The choice is {coin_side}")
    return HttpResponse(f"{coin_side}")


def random_number_cube(request):
    result_cube = random.randint(1, 6)
    logger.info(f"The cube side is {result_cube}")
    return HttpResponse(f'random number: {result_cube}')


def random_number_hundred(request):
    result_num = random.randint(1, 100)
    logger.info(f"The random number is {result_num}")
    return HttpResponse(f'random number: {result_num}')


def get_last_results(request):
    list_of_coin_values = Coin.get_last_results()
    if list_of_coin_values:
        result_string = '<br>'.join(str(value) for value in list_of_coin_values)
        return HttpResponse(result_string)
    else:
        return HttpResponse("No results found.")
