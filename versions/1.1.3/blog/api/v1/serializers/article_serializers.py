# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.article_models import Article


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.ReadOnlyField(source="category.name")
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Article
        fields = ('category', 'title', 'author', 'image', 'body',
                  'date_published'
                  )