# Core Django imports.
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

# Third-party Django app imports.
from model_mommy import mommy

# Blog application imports.
from blog.models.article_models import Article


class ArticleTestCase(TestCase):
    """
      Class to test the article model.
    """

    def setUp(self):
        """
          Set up all the tests using model_mommy.
        """
        self.article = mommy.make(_model=Article, body="Test")

    def test_if_article_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.article.__str__(), self.article.title)

    def test_if_article_returns_the_right_slug(self):
        self.assertEqual(self.article.slug, slugify(self.article.title))

    def test_article_get_absolute_url(self):
        self.assertEquals(self.article.get_absolute_url(),
                          reverse('blog:article_detail', kwargs={'username': self.article.author.username.lower(),
                                                                 'slug': self.article.slug}))
