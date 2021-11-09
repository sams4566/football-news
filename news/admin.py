from django.contrib import admin
from .models import Article, Comment

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display = ('name', 'approved', 'time_created', 'updated_time', 'author',)
    actions = ['approve_selected_articles']
    prepopulated_fields = {'slug': ('name',)}
    
    def approve_selected_articles(self, request, list_of_articles):
        list_of_articles.update(approved=True)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('post', 'time_created',)
    list_filter = ('post', 'time_created',)
