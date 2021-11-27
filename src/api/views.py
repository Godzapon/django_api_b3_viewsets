from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status, viewsets
from .serializers import ArticleSerializer, CommentSerializer
from .models import Article, Comment


# Create your views here.
def api_index(request, id):
    return HttpResponse(id)


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


@api_view(['GET', 'POST'])
def comments(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        comments = Comment.objects.filter(article=article)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        request.data['article'] = article.id
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.article = article
            serializer.article_id = article.id
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
@api_view(['DELETE', 'GET'])
def comment(request, article_id, comment_id):
    try:
        Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    try:
        comment = Comment.objects.get(pk=comment_id)
    except Comment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        try:
            comment.delete()
        except:
            return Response(status=status.HTTP_409_CONFLICT)
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
