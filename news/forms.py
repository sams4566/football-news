from .models import Article
from django import forms

class ArticleDetails(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name', 'slug', 'content', 'article_image', 'author',)

# class CommentForm(forms.ModelForm):
#     class Meta: 
#         model = Comment
#         fields = ('body',)