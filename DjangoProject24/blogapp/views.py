import logging
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Author, Article, Comment
from .forms import AuthorForm, ArticleForm, CommentForm
from faker import Faker

logger = logging.getLogger(__name__)
fake = Faker()
fake_ru = Faker('ru_RU')


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


# Представление для вывода всех авторов из базы
def view_all_authors(request):
    authors = Author.objects.all()
    return render(request, 'blogapp/view_all_authors.html', {'authors': authors})


# Представление для вывода всех статей из базы
def view_all_articles(request):
    articles = Article.objects.all()
    return render(request, 'blogapp/view_all_articles.html', {'articles': articles})


# Представление для вывода всех комментариев из базы
def view_all_comments(request):
    comments = Comment.objects.all()
    return render(request, 'blogapp/view_all_comments.html', {'comments': comments})


# Выводит статью по её ID
def detail_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    article.views += 1
    article.save()
    comments = Comment.objects.filter(article=article).order_by('-updated_at')
    return render(request, 'blogapp/detail_article.html', {'article': article, 'comments': comments})


# Выводит автора по его ID
def detail_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'blogapp/detail_author.html', {'author': author})


# Выводит комментарий по его ID
def detail_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    return render(request, 'blogapp/detail_comment.html', {'comment': comment})


# Форма для добавления нового автора
def add_author_form(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author = author_form.save()
            logger.info(f'Добавлен новый автор {author.full_name}')
            return render(request, 'blogapp/add_author_form.html', {'response': 'Автор успешно добавлен'})
    else:
        author_form = AuthorForm()
    return render(request, 'blogapp/add_author_form.html', {'author_form': author_form})


# Форма для добавления новой статьи
def add_article_form(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save()
            logger.info(f'Добавлена новая статья ID: {article.pk} — {article.title}')
            return render(request, 'blogapp/add_article_form.html', {'response': 'Статья успешно добавлена'})
    else:
        article_form = ArticleForm()
    return render(request, 'blogapp/add_article_form.html', {'article_form': article_form})


# Форма для добавления нового комментария
def add_comment_form(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.article = article  # Присваиваем комментарию статью
            comment.save()
            logger.info(f'Добавлен новый комментарий {comment.content}')
            return render(request, 'blogapp/add_comment_form.html', {'response': 'Комментарий успешно добавлен'})
    else:
        comment_form = CommentForm()
    return render(request, 'blogapp/add_comment_form.html', {'comment_form': comment_form, 'article': article})


# Форма редактирования автора
def edit_author_form(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, instance=author)
        if author_form.is_valid():
            author_form.save()
            logger.info(f'Автор ID:{author.pk} успешно отредактирован')
            return redirect('detail_author', author_id=author_id)
    else:
        author_form = AuthorForm(instance=author)
    return render(request, 'blogapp/edit_author_form.html', {'author_form': author_form, 'author': author})


# Форма редактирования статьи
def edit_article_form(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            logger.info(f'Статья {article.pk} успешно отредактирована')
            return redirect('detail_article', article_id=article_id)
    else:
        article_form = ArticleForm(instance=article)
    return render(request, 'blogapp/edit_article_form.html', {'article_form': article_form, 'article': article})


def edit_comment_form(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment_form.save()
            logger.info(f'Комментарий ID:{comment.pk} успешно отредактирован')
            return redirect('detail_comment', comment_id=comment_id)
    else:
        comment_form = CommentForm(instance=comment)
    return render(request, 'blogapp/edit_comment_form.html', {'comment_form': comment_form, 'comment': comment})


def delete_author(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    if request.method == 'POST':
        author.delete()
        logger.info(f'Автор {author_id} успешно удален')
        return redirect('all_authors')
    return render(request, 'blogapp/delete_author_confirm.html', {'author': author})


def delete_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == 'POST':
        article.delete()
        logger.info(f'Комментарий ID:{article_id} успешно удален')
        return redirect('all_articles')
    return render(request, 'blogapp/delete_article_confirm.html', {'article': article})


def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        comment.delete()
        logger.info(f'Комментарий ID:{comment_id} успешно удален')
        return redirect('all_comments')
    return render(request, 'blogapp/delete_comment_confirm.html', {'comment': comment})


def view_comments_by_article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article)
    return render(request, 'blogapp/view_comments_by_article.html', {'article': article, 'comments': comments})


def author_articles(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    articles = Article.objects.filter(author=author)
    return render(request, 'blogapp/author_articles.html', {'author': author, 'articles': articles})
