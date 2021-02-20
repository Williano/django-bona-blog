# Third-party apps import
from rest_framework import generics

# Blog app imports
from blog.models.article_models import Article
from ..serializers.article_serializers import ArticleSerializer


class ArticleList(generics.ListAPIView):
    queryset = Article.objects.filter(status='PUBLISHED')
    serializer_class = ArticleSerializer


class CategoryArticleList(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        articles = Article.objects.filter(category__name=category_name,
                                          status='PUBLISHED'
                                          )
        return articles

