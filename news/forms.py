from .models import Article, Comment
from django import forms

class ArticleDetails(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name',)

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body',)