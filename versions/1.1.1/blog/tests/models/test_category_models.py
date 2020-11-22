# Core Django imports.
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

# Third-party Django app imports.
from model_mommy import mommy

# Blog application imports.
from blog.models.category_models import Category


class CategoryTestCase(TestCase):
    """
      Class to test the category model.
    """

    def setUp(self):
        """
          Set up all the tests using model_mommy.
        """
        self.category = mommy.make(Category)

    def test_if_category_returns_the_right_human_readable_representation(self):
        self.assertEqual(self.category.__str__(), self.category.name)

    def test_if_category_returns_the_right_slug(self):
        self.assertEqual(self.category.slug, slugify(self.category.name))

    def test_category_get_absolute_url(self):
        self.assertEquals(self.category.get_absolute_url(),
                          reverse('blog:category_articles',
                                  kwargs={'slug': self.category.slug}))

