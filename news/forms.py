from .models import Article, Comment
from django import forms

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'slug', 'content', 'image', 'author',)

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body',)