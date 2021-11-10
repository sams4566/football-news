from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_article")
    headline = models.CharField(unique=True, max_length=250)
    approved = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=250)
    time_created = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    content = models.TextField()
    image = CloudinaryField('image', default='default_image')
    
    def __str__(self):
        return self.headline

class Comment(models.Model):
    post = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="post_comment")
    body = models.TextField()
    time_created_comment = models.DateTimeField(auto_now_add=True)
    users_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.body