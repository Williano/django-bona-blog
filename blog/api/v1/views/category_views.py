# Third-party apps import
from rest_framework import generics

# Local application imports
from blog.models.article_models import Category
from ..serializers.category_serializers import CategorySerializer


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
