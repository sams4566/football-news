from .models import Article
from django import forms

class ArticleDetails(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('name',)