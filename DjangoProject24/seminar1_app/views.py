from django.shortcuts import render
from django.http import HttpResponse
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
