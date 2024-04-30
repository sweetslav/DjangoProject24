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


def heads_or_tails(request, count):
    results = []
    for _ in range(count):
        coin_side = random.choice(["Орёл", "Решка"])
        results.append(coin_side)
        coin = Coin(side=coin_side)
        coin.save()
        logger.info(f"Результат броска: {coin_side}")

    context = {
        'game_name': "Орёл и решка",
        'results': results
    }
    return render(request, "gameapp/games.html", context)


def random_number_cube(request, count):
    results = []
    for _ in range(count):
        result_cube = random.randint(1, 6)
        results.append(result_cube)
        logger.info(f"Результат броска кубика: {result_cube}")

    context = {
        'game_name': "Игральные кости",
        'results': results
    }
    return render(request, "gameapp/games.html", context)


def random_number_hundred(request, count):
    results = []
    for _ in range(count):
        result_num = random.randint(1, 100)
        results.append(result_num)
        logger.info(f"Случайное число: {result_num}")

    context = {
        'game_name': "Случайное число",
        'results': results
    }
    return render(request, "gameapp/games.html", context)


def get_last_results(request):
    list_of_coin_values = Coin.get_last_results()
    if list_of_coin_values:
        result_string = '<br>'.join(str(value) for value in list_of_coin_values)
        return HttpResponse(result_string)
    else:
        return HttpResponse("No results found.")
