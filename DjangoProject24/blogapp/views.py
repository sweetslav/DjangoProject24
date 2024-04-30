from django.shortcuts import render
from django.http import HttpResponse
from .models import Author
import logging
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()
fake_ru = Faker('ru_RU')


def read_authors(request):
    logger.info("Someone has visited the Blog / Read Authors page ")
    return HttpResponse("<h1>This is read Authors page</h1><br>")


def create_fake_author_male():
    fake_fname = fake_ru.first_name_male()
    fake_lname = fake_ru.last_name_male()
    fake_email = f'{fake_fname}{fake_lname}@example.com'
    # fake_email = fake_ru.fake_email() # Создает случайную почту
    fake_bday = fake_ru.date_of_birth(minimum_age=18, maximum_age=65)
    fake_address = fake_ru.address()
    fake_job = fake_ru.job()
    fake_bio = f'{fake_fname} {fake_lname} родился {fake_bday.strftime("%d.%m.%Y")} ' \
               f'в городе {fake_address.split(",")[0]}. ' \
               f'Он работает {fake_job} и имеет почту {fake_email}.'

    author = Author(
        first_name=fake_fname,
        last_name=fake_lname,
        email=fake_email,
        birthday=fake_bday,
        biography=fake_bio
    )
    author.save()
    return author


def create_fake_author_female():
    fake_fname = fake_ru.first_name_female()
    fake_lname = fake_ru.last_name_female()
    fake_email = f'{fake_fname}{fake_lname}@example.com'
    #  fake_email = fake_ru.fake_email() # Создает случайную почту
    fake_bday = fake_ru.date_of_birth(minimum_age=18, maximum_age=65)
    fake_address = fake_ru.address()
    fake_job = fake_ru.job()
    fake_bio = f'{fake_fname} {fake_lname} родился {fake_bday.strftime("%d.%m.%Y")} ' \
               f'в городе {fake_address.split(",")[0]}. ' \
               f'Он работает {fake_job} и имеет почту {fake_email}.'

    author = Author(
        first_name=fake_fname,
        last_name=fake_lname,
        email=fake_email,
        birthday=fake_bday,
        biography=fake_bio
    )
    author.save()
    return author


def write_authors(request):
    logger.info("Someone has visited the Blog / Write Authors page ")
    count = 10
    for i in range(count):
        create_fake_author_male()
        create_fake_author_female()
    logger.info("Created new authors")
    return HttpResponse("Created 20 new authors")


def base_html(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'blogapp/about.html')


def aboutme(request):
    context = {'name': 'Святослав', 'last_name': 'Кривошеев', 'birthday': '04.02.1995',
               'email': 'sweetslav@example.com'}
    return render(request, 'blogapp/about.html', context)
