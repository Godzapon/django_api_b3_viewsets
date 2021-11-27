from rest_framework import serializers
from .models import Article, Comment


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', 'author', 'date')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        #fields = '__all__'
        fields = ('id', 'title', 'content')
