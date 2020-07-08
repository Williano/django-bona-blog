# Core Django Imports
from django.urls import path

# Blog application imports
from blog.api.v1.views.category_views import CategoryList
from blog.api.v1.views.article_views import ArticleList, CategoryArticleList

urlpatterns = [
    path('categories/', CategoryList.as_view()),
    path('articles/', ArticleList.as_view()),
    path('<str:category_name>/', CategoryArticleList.as_view()),
]

