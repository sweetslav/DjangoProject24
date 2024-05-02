from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Article
from .forms import AuthorForm
import logging
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()
fake_ru = Faker('ru_RU')


# Представление для создания 10 авторов в базу
def write_authors(request):
    logger.info("Someone has visited the Blog / Write Authors page ")
    count = 10
    for i in range(count):
        create_fake_author_male()
        create_fake_author_female()
    logger.info("Created new authors")
    return HttpResponse("Created 20 new authors")


# Представление для базового шаблона сайта
def base_html(request):
    return render(request, 'base.html')


def about(request):
    return render(request, 'blogapp/about.html')


# Страница обо мне
def aboutme(request):
    context = {'name': 'Святослав', 'last_name': 'Кривошеев', 'birthday': '04.02.1995',
               'email': 'sweetslav@example.com'}
    return render(request, 'blogapp/about.html', context)


# Форма для добавления нового автора
def add_author_form(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author = author_form.save()
            logger.info(f'Добавлен новый автор {author.first_name} {author.last_name}')
            return render(request, 'blogapp/add_author_form.html', {'response': 'Автор успешно добавлен'})
    else:
        author_form = AuthorForm()
    return render(request, 'blogapp/add_author_form.html', {'author_form': author_form})
