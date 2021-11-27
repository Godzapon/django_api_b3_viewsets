from django.db import models

# Create your models here.
from django.utils.text import slugify


class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    author = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(blank=True)


class Comment(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
