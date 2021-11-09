from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="news_article")
    name = models.CharField(unique=True, max_length=250)
    approved = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, max_length=250)
    time_created = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    article_image = CloudinaryField('image', default='default_image')
    content = models.TextField()


    def __str__(self):
        return self.name

# class Comment(models.Model):
#     body = models.TextField()

#     def __str__(self):
#         return self.body