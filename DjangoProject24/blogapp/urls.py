from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    # Статьи
    path('articles/', views.view_all_articles, name='all_articles'),
    path('article/add/', views.add_article_form, name='add_article'),
    path('article/<int:article_id>/', views.detail_article, name='detail_article'),
    path('article/<int:article_id>/edit/', views.edit_article_form, name='edit_article'),
    path('article/<int:article_id>/delete/', views.delete_article, name='delete_article'),
    path('article/<int:article_id>/comment/', views.add_comment_form, name='add_comment'),
    path('article/<int:article_id>/comments', views.view_comments_by_article, name='view_comments_by_article'),

    # Авторы
    path('authors/', views.view_all_authors, name='all_authors'),
    path('author/add/', views.add_author_form, name='add_author'),
    path('author/<int:author_id>/', views.detail_author, name='detail_author'),
    path('author/<int:author_id>/edit/', views.edit_author_form, name='edit_author'),
    path('author/<int:author_id>/articles/', views.author_articles, name='author_articles'),
    path('author/<int:author_id>/delete/', views.delete_author, name='delete_author'),

    # Комментарии
    path('comments/', views.view_all_comments, name='all_comments'),
    path('comment/<int:comment_id>/edit/', views.edit_comment_form, name='edit_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/', views.detail_comment, name='detail_comment'),

    # О сайте и обо мне
    path('about/', views.about, name='about'),
    path('about/me/', views.aboutme, name='aboutme'),
]

