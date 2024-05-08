from django.db import models
from django.utils import timezone


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()

    def __str__(self):
        return (f'Name: {self.first_name},\n'
                f'Last name: {self.last_name},\n'
                f'Email: {self.email},\n'
                f'Birthday: {self.birthday}')

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class Article(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    category = models.CharField(max_length=100)
    views = models.IntegerField(default=0)
    published = models.BooleanField(default=False)

    def count_comments_for_article(self):
        return self.comments.count()

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='comments')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @staticmethod
    def count_comments_for_article(article_id):
        return Comment.objects.filter(article_id=article_id).count()

    def __str__(self):
        return f'{self.author.full_name} добавил комментарий к статье: {self.article.title}'
