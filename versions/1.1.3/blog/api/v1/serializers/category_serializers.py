# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.article_models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'image')


