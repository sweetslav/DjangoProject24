import logging
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Author, Article, Comment
from .forms import AuthorForm
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


def get_articles_by_author_name(author_name, limit=None, sort_by='-published_date'):
    author = Author.objects.filter(full_name=author_name).first()
    if author:
        articles = Article.objects.filter(author=author).order_by(sort_by)
        if limit:
            articles = articles[:limit]
        return articles
    else:
        return []


def get_comments_by_author_name(author_name, limit=None, sort_by='-created_at'):
    author = Author.objects.filter(full_name=author_name).first()
    if author:
        comments = Comment.objects.filter(author=author).order_by(sort_by)
        if limit:
            comments = comments[:limit]
        return comments
    else:
        return []


def get_comments_by_article_title(article_title, limit=None, sort_by='-created_at'):
    article = Article.objects.filter(title=article_title).first()
    if article:
        comments = Comment.objects.filter(article=article).order_by(sort_by)
        if limit:
            comments = comments[:limit]
        return comments
    else:
        return []


# Представление для вывода всех заметок автора по его айди
def author_articles(request, author_id=None):
    if author_id is not None:
        author = get_object_or_404(Author, author_id)
        articles = Article.objects.filter(author=author).order_by('-published_date')
    else:
        author = None
        articles = Article.objects.all().order_by('-published_date')
    return render(request, 'blogapp/author_articles.html', {'author': author, 'articles': articles})


def view_all_authors(request):
    authors = Author.objects.all()
    return render(request, 'blogapp/view_all_authors.html', {'authors': authors})


def view_all_articles(request):
    articles = Article.objects.all()
    return render(request, 'blogapp/view_all_articles.html', {'articles': articles})


def view_all_comments(request):
    comments = Comment.objects.all()
    return render(request, 'blogapp/view_all_comments.html', {'comments': comments})
