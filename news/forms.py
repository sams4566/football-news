from .models import Article, Comment, Category
from django import forms


class CategoryForm(forms.ModelForm):
    class Meta: 
        model = Category
        fields = ('category_name',)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('headline', 'image',)

class CommentForm(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('body',)