from django.urls import path
from rest_framework import routers

from .views import ArticleViewSet, comments, comment

api_router = routers.DefaultRouter()
api_router.register('articles', ArticleViewSet)

urlpatterns = [
    path("articles/<int:article_id>/comments", comments),
    path("articles/<int:article_id>/comments/<int:comment_id>", comment),
]
