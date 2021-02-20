# Core Django imports.
from django.contrib.auth.models import User
from django.forms.models import model_to_dict
from django.test import Client
from django.test import TestCase
from django.urls import reverse

# Third-party Django app imports.
from model_mommy import mommy

# Blog application imports.
from blog.models.article_models import Article
from blog.models.category_models import Category


class CategoriesListViewTestCase(TestCase):
    """
    Class to test the list of all categories
    """

    def setUp(self):
        """
        Set up all the tests using django client.

        Model mommy creates five categories and store them in a list called
        categories. You can access them with their indices.
        """
        self.client = Client()
        self.categories = mommy.make(Category, _quantity=5)

    def test_categories_list_view_status_code(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(response.status_code, 200)

    def test_categories_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(response.status_code, 200)

    def test_if_categories_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertTemplateUsed(response, 'blog/category/categories_list.html')

    def test_if_categories_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, "<title>BONA</title>")

    def test_if_categories_list_view_returns_the_right_number_of_categories(self):
        response = self.client.get(reverse('blog:categories_list'))
        self.assertEqual(len(response.context_data['categories']), 5)

    # def test_if_categories_list_view_returns_the_right_category_details(self):
    #     response = self.client.get(reverse('blog:categories_list'))
    #     self.assertEqual(response.context_data['categories'][0].name,
    #                      self.categories[0].name)
    #     self.assertEqual(response.context_data['categories'][0].slug,
    #                      self.categories[0].slug)


class CategoryArticlesListViewTestCase(TestCase):
    """
    Class to test a particular category's articles.
    """

    def setUp(self):
        """
        Set up all the tests using django client and model_mommy.
        """
        self.client = Client()
        self.category = mommy.make(Category)
        self.articles = mommy.make(Article, body="Test", category=self.category, _quantity=5)

    def test_category_article_list_view_status_code(self):
        response = self.client.get(self.category.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_category_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:category_articles',
                                           kwargs={'slug': self.category.slug}))
        self.assertEqual(response.status_code, 200)

    def test_if_category_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:category_articles',
                                           kwargs={'slug': self.category.slug}))
        self.assertTemplateUsed(response, 'blog/category/category_articles.html')
    #
    # def test_if_category_articles_list_view_returns_the_right_number_of_articles(self):
    #     response = self.client.get(reverse('blog:category_articles',
    #                                        kwargs={'slug': self.category.slug}))
    #     self.assertEqual(len(response.context["articles"]), 5)

    # def test_if_category_articles_list_view_returns_the_right_category_details(self):
    #     response = self.client.get(self.category.get_absolute_url())
    #     self.assertEqual(response.context_data["articles"][0].category,
    #                      self.category)
    #     self.assertEqual(response.context_data["articles"][0].category.name,
    #                      self.category.name)
    #     self.assertEqual(response.context_data["articles"][0].category.slug,
    #                      self.category.slug)
    #     self.assertEqual(response.context_data["articles"][0].category.image,
    #                      self.category.image)

    # def test_if_category_articles_list_view_returns_the_right_article_details(self):
    #     """
    #     This test checks if the view returns the right articles according to the
    #     date they were published.
    #
    #     In the setup, model mommy creates five articles and store
    #     them in a list called articles. So the last article in the list will
    #     be the first article in the list view since it was created last by model
    #     mommy.
    #     The list view orders articles according to the time they were published
    #     so the last article in the articles list will be displayed first in the
    #     view.
    #     """
    #     response = self.client.get(self.category.get_absolute_url())
    #     self.assertEqual(response.context_data['articles'][0].category,
    #                      self.articles[4].category)
    #     self.assertEqual(response.context_data['articles'][0].title,
    #                      self.articles[4].title)
    #     self.assertEqual(response.context_data['articles'][0].slug,
    #                      self.articles[4].slug)
    #     self.assertEqual(response.context_data['articles'][0].author,
    #                      self.articles[4].author)
    #     self.assertEqual(response.context_data['articles'][0].image,
    #                      self.articles[4].image)
    #     self.assertEqual(response.context_data['articles'][0].body,
    #                      self.articles[4].body)
    #     self.assertEqual(response.context_data['articles'][0].date_published,
    #                      self.articles[4].date_published)
    #     self.assertEqual(response.context_data['articles'][0].date_created,
    #                      self.articles[4].date_created)
    #     self.assertEqual(response.context_data['articles'][0].status,
    #                      self.articles[4].status)



# class CategoryCreateViewTest(TestCase):
#     """
#     Test to check if the create create view works as required.
#     """
#     def setUp(self):
#         """
#         Model mommy creates a category.
#
#         :return: an article
#         """
#         self.client = Client()
#         self.author = mommy.make(User)
#         test_user1 = User.objects.create_user(username='testuser1',
#                                               password='1X<ISRUkw+tuK')
#         test_user1.save()
#
#     def test_redirect_if_not_logged_in(self):
#         response = self.client.get(reverse("article:category_create"))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, "/account/login/?next=/category/new/")
#
#     def test_logged_in_uses_correct_template(self):
#         self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('article:category_create'))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertTemplateUsed(response, "article/category_form.html")
#
#     def test_create_a_new_category_with_valid_data(self):
#         """
#         Before posting we assert that there is no Category in the database.
#
#         We make sure that a Category is created in the database on post by
#         checking that count of Category has been increased to 1.
#
#         We also check if the category returns the right details that was posted.
#
#         :return: Assertions:
#         """
#         self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#
#         self.assertEqual(Category.objects.count(), 0)
#
#         category = mommy.make(Category)
#         category1 = model_to_dict(category)
#         response = self.client.post(reverse('article:category_create'), category1)
#         print(response.context_data)
#         self.assertEqual(response.status_code, 200)
#
#         response = self.client.get(category.get_absolute_url())
#         # print(response.context_data)
#         # self.assertEqual(response.context_data['category'].name,
#         #                  category.name)
#         # self.assertEqual(response.context_data['category'].slug,
#         #                  category.slug)
#         #
#         # self.assertEqual(category.objects.count(), 1)
#
#     def test_create_a_new_category_with_invalid_data(self):
#         """
#          Since we posted an invalid form, we expect to remain on the same page.
#          So asserted for status code of 200.
#
#          We expect an error to be present on the title field.
#          We expect an error to be present on the body field.
#
#         :return Assertions:
#         """
#         self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#
#         self.assertEqual(Category.objects.count(), 0)
#
#         category = mommy.make(Category)
#         category1 = model_to_dict(category)
#         response = self.client.post(reverse('article:category_create'), category1)
#         # print(response.context_data)
#         # self.assertEqual(response.status_code, 200)
#         # self.assertFormError(response, "form", "name",
#         #                      "This field is required.")
