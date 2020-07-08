# Third party imports.
from rest_framework import serializers

# Local application imports
from blog.models.author_models import Profile


class AuthorProfile(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'image')
