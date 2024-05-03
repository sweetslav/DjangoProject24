from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.view_all_articles, name='all_articles'),  # Страница со списком всех статей
    path('authors/', views.view_all_authors, name='all_authors'),  # Страница со списком всех авторов
    path('comments/', views.view_all_comments, name='all_comments'),  # Страница со списком всех комментариев
    path('author/add/', views.add_author_form, name='add_author'),  # Страница для добавления нового автора
    path('article/add/', views.add_article_form, name='add_article'), # Страница для добавления новой статьи
    path('article/<int:article_id>/comment/', views.add_comment_form, name='add_comment'), # Страница для добавления нового комментария
    path('about/', views.about, name='about'),
    path('about/me/', views.aboutme, name='aboutme'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'), # Страница с деталями конкретной статьи
    path('article/<int:article_id>/edit/', views.edit_article_form, name='edit_article'), # Страница с формой для редактирования статьи
    # path('article/<int:article_id>/delete/', views.delete_article_confirm, name='delete_article'), # Страница с формой для удаления статьи
    # path('author/<int:author_id>/articles/', views.author_articles, name='author_articles'), # Страница со списком статей конкретного автора
    path('author/<int:author_id>/', views.author_detail, name='author_detail'), # Страница с деталями конкретного автора
    path('author/<int:author_id>/edit/', views.edit_author_form, name='edit_author'), # Страница с формой для редактирования автора
    # path('author/<int:author_id>/delete/', views.delete_author_confirm, name='delete_author'), # Страница с формой для удаления автора
    # path('comment/<int:comment_id>/edit/', views.edit_comment_form, name='edit_comment'), # Страница с формой для редактирования комментария
    # path('comment/<int:comment_id>/delete/', views.delete_comment_confirm, name='delete_comment'), # Страница с формой для удаления комментария
]
