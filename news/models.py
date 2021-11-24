from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
import datetime


class Category(models.Model):
    category_name = models.CharField(max_length=250)
    approve_category = models.BooleanField(default=False)
    category_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="category_author")

    def __str__(self):
            return self.category_name

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_article")
    headline = models.CharField(max_length=250)
    extract = models.TextField(max_length=100)
    approved = models.BooleanField(default=False)
    time_created = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField("image", default="default_image")
    upvote = models.ManyToManyField(User, blank=True, related_name="news_upvotes")
    downvote = models.ManyToManyField(User, blank=True, related_name="news_downvotes")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_article")

    def upvotes_count(self):
        return self.upvote.count()

    def downvotes_count(self):
        return self.downvote.count()

    def votes_count(self):
        return self.upvote.count() - self.downvote.count()

    def upvote_user(self):
        return [upvote.id for upvote in self.upvote.all()]

    def downvote_user(self):
        return [downvote.id for downvote in self.downvote.all()]
        
    def __str__(self):
        return self.headline

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="article_comment")
    body = models.TextField()
    time_created_comment = models.DateTimeField(auto_now_add=True)
    users_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="users_name")

    def __str__(self):
        return self.body