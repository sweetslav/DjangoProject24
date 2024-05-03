from django import forms
from .models import Author, Article, Comment


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'email', 'biography', 'birthday']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'biography': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 40}),
            'birthday': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'content', 'published_date', 'category', 'views', 'published']
        widgets = {}


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {}
