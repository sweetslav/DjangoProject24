from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('write_authors/', views.write_authors, name='write_authors'),
    path('about/', views.about, name='about'),
    path('about/me/', views.aboutme, name='aboutme'),
    path('author/add/', views.add_author_form, name='add_author_form'),
    path('author/all', views.view_all_authors, name='view_all_authors'),
    path('article/all', views.view_all_articles, name='view_all_articles'),
    path('comment/all', views.view_all_comments, name='view_all_comments'),
]
