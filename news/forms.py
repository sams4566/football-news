from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('headline', 'slug', 'content', 'image', 'author',)

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body', 'users_name',)