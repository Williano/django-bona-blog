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


class ArticleListViewTestCase(TestCase):
    """
    Class to test the list of all articles.
    """

    def setUp(self):
        """
        Set up all the tests using django client.

        Model mommy creates a single category called category.

        Model mommy creates four articles and store them in a list called
        articles. So the last article in the list will be the first article
        in the list view since it was created last by model mommy. You can
        access the articles using their indices.
        """
        self.client = Client()
        self.category = mommy.make(Category)
        self.articles = mommy.make(Article,
                                   body="Test",
                                   status='PUBLISHED',
                                   category=self.category,
                                   _quantity=4)

    def test_article_list_view_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_article_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:home'))
        self.assertEqual(response.status_code, 200)

    def test_if_article_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:home'))
        self.assertTemplateUsed(response, 'blog/article/home.html')

    def test_if_article_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get('')
        self.assertNotContains(response, "<title>BONA</title>")

    def test_if_article_list_view_returns_the_right_number_of_categories(self):
        response = self.client.get('')
        self.assertEqual(len(response.context_data['categories']), 1)

    def test_if_article_list_view_returns_the_right_category_details(self):
        response = self.client.get('')
        self.assertEqual(response.context_data['categories'][0],
                         self.category)
        self.assertEqual(response.context_data['categories'][0].name,
                         self.category.name)
        self.assertEqual(response.context_data['categories'][0].slug,
                         self.category.slug)
        self.assertEqual(response.context_data['categories'][0].image,
                         self.category.image)

    def test_if_article_list_view_returns_the_right_number_of_articles(self):
        response = self.client.get('')
        self.assertEqual(len(response.context_data['articles']), 4)

    def test_if_article_list_view_returns_the_right_article_details(self):
        """
        This test checks if the view returns the right articles according to the
        date they were published.

        In the setup, model mommy creates four articles and store
        them in a list called articles. So the last article in the list will
        be the first article in the list view since it was created last by model
        mommy.
        The list view orders articles according to the time they were published.
        """
        response = self.client.get('')
        self.assertEqual(response.context_data['categories'][0],
                         self.category)
        self.assertEqual(response.context_data['categories'][0].name,
                         self.category.name)
        self.assertEqual(response.context_data['articles'][0].category,
                         self.articles[3].category)
        self.assertEqual(response.context_data['articles'][0].title,
                         self.articles[3].title)
        self.assertEqual(response.context_data['articles'][0].slug,
                         self.articles[3].slug)
        self.assertEqual(response.context_data['articles'][0].author,
                         self.articles[3].author)
        self.assertEqual(response.context_data['articles'][0].image,
                         self.articles[3].image)
        self.assertEqual(response.context_data['articles'][0].body,
                         self.articles[3].body)
        self.assertEqual(response.context_data['articles'][0].date_published,
                         self.articles[3].date_published)
        self.assertEqual(response.context_data['articles'][0].date_created,
                         self.articles[3].date_created)
        self.assertEqual(response.context_data['articles'][0].status,
                         self.articles[3].status)


class ArticleDetailViewTestCase(TestCase):
    """
    Test to check if the article detail view works as required.
    """
    def setUp(self):
        """
        Model mommy creates an article.

        :return: an article
        """
        self.client = Client()
        self.article = mommy.make(_model=Article, body="Test")

    def test_article_detail_view_absolute_url(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_article_detail_view_url_by_name(self):
        response = self.client.get(reverse('blog:article_detail',
                                           kwargs={'slug': self.article.slug,
                                                   'username': self.article.author.username.lower()
                                                   }))
        self.assertEqual(response.status_code, 200)

    def test_if_categories_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:article_detail',
                                           kwargs={'slug': self.article.slug,
                                                   'username': self.article.author.username.lower()}))
        self.assertTemplateUsed(response, 'blog/article/article_detail.html')

    def test_if_article_detail_view_returns_the_right_article_details(self):
        response = self.client.get(self.article.get_absolute_url())
        self.assertEqual(response.context["article"].category,
                         self.article.category)
        self.assertEqual(response.context["article"].title, self.article.title)
        self.assertEqual(response.context["article"].slug, self.article.slug)
        self.assertEqual(response.context["article"].author,
                         self.article.author)
        self.assertEqual(response.context["article"].image, self.article.image)
        self.assertEqual(response.context["article"].body, self.article.body)
        self.assertEqual(response.context["article"].date_published,
                         self.article.date_published)
        self.assertEqual(response.context["article"].date_created,
                         self.article.date_created)
        self.assertEqual(response.context["article"].status,
                         self.article.status)


class ArticleSearchListViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.articles = mommy.make(Article, _quantity=5, body="Test", status='PUBLISHED')

    def test_article_search_list_view_status_code(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_article_search_list_view_url_by_name(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertEqual(response.status_code, 200)

    def test_article_search_list_view_uses_correct_template(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertTemplateUsed(response, 'blog/article/article_search_list.html')

    def test_article_search_list_view_does_not_contain_incorrect_html(self):
        response = self.client.get(reverse('blog:article_search_list_view'))
        self.assertNotContains(response, 'blog/article/categories_list_view.html')

    def test_article_search_list_view_returns_the_right_query_results(self):
        response = self.client.get(f"/article/search/?q={self.articles[0].title}")
        self.assertEqual(len(response.context['search_results']), 1)
        self.assertEqual(response.context['search_results'][0].slug,
                         self.articles[0].slug)

    def test_article_search_list_view_returns_all_articles_if_nothing_is_typed_in_the_search_input(self):
        response = self.client.get(f"/article/search/?q=")
        self.assertEqual(len(response.context['search_results']), 0)


class ArticleCreateViewTestCase(TestCase):
    """
    Test to check if the article create view works as required.
    """
    def setUp(self):
        """
        Model mommy creates an article.

        :return: an article
        """
        self.client = Client()
        self.author = mommy.make(User)
        test_user1 = User.objects.create_user(username='testuser1',
                                              password='1X<ISRUkw+tuK')
        test_user1.save()

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse("blog:article_write"))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, "/account/login/?next=/me/article/write/")

    def test_logged_in_uses_correct_template(self):
        self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
        response = self.client.get(reverse('blog:article_write'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(str(response.context['user']), 'testuser1')
        self.assertTemplateUsed(response, "dashboard/author/article_create_form.html")

    # def test_create_a_new_article_with_valid_data(self):
    #     """
    #     Before posting we assert that there is no Article in the database.
    #
    #     We make sure that a Article is created in the database on post by
    #     checking that count of Article has been increased to 1.
    #
    #     We also check if the article returns the right details that was posted.
    #
    #     :return: Assertions:
    #     """
    #     self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
    #
    #     self.assertEqual(Article.objects.count(), 0)
    #
    #     article = mommy.make(Article, body="test", image_credit="new", author=self.author, status='PUBLISHED')
    #     article1 = model_to_dict(article)
    #     response = self.client.post(reverse('blog:article_write'), article1)
    #
    #     self.assertEqual(response.status_code, 200)
    #
    #     response = self.client.get(article.get_absolute_url())
    #     self.assertEqual(response.['article'].category,
    #                      article.category)
    #     self.assertEqual(response.context_data['article'].title,
    #                      article.title)
    #     self.assertEqual(response.context_data['article'].slug,
    #                      article.slug)
    #     self.assertEqual(response.context_data['article'].author,
    #                      article.author)
    #     self.assertEqual(response.context_data['article'].image,
    #                      article.image)
    #     self.assertEqual(response.context_data['article'].body,
    #                      article.body)
    #     self.assertEqual(response.context_data['article'].date_published,
    #                      article.date_published)
    #     self.assertEqual(response.context_data['article'].date_created,
    #                      article.date_created)
    #     self.assertEqual(response.context_data['article'].status,
    #                      article.status)
    #
    #     self.assertEqual(Article.objects.count(), 1)
    #
    # def test_can_create_a_new_article_with_invalid_data(self):
    #     """
    #      Since we posted an invalid form, we expect to remain on the same page.
    #      So asserted for status code of 200.
    #
    #      We expect an error to be present on the title field.
    #      We expect an error to be present on the body field.
    #
    #     :return Assertions:
    #     """
    #     self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
    #
    #     self.assertEqual(Article.objects.count(), 0)
    #
    #     article = mommy.make(Article, title='', body='', image_credit='', status='PUBLISHED')
    #     article1 = model_to_dict(article)
    #     response = self.client.post(reverse('blog:article_write'), article1)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertFormError(response, "form", "title",
    #                          "This field is required.")
    #     self.assertFormError(response, "form", "body",
    #                          "This field is required.")


# class ArticleDeleteViewTest(TestCase):
#     """
#     Test to check if the article delete view works as required.
#     """
#     def setUp(self):
#         """
#         Model mommy creates five articles.
#
#         :return: articles
#         """
#         self.client = Client()
#         self.author = mommy.make(User)
#         test_user1 = User.objects.create_user(username='testuser1',
#                                               password='1X<ISRUkw+tuK')
#         test_user1.save()
#         test_user2 = User.objects.create_user(username='testuser2',
#                                               password='1X<ISRUkw+tuK')
#         test_user2.save()
#         self.articles = mommy.make(Article, author=test_user1,  _quantity=5)
#
#     def test_article_author_can_delete_article(self):
#         self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#
#         self.assertEqual(Article.objects.count(), 5)
#
#         response = self.client.post(reverse('blog:article_delete',
#                                     kwargs={'slug': self.articles[0].slug}))
#
#         self.assertEqual(Article.objects.count(), 4)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, "/")
#
#     def test_unauthorized_author_cannot_delete_article(self):
#         self.client.login(username='testuser2', password='1X<ISRUkw+tuK')
#
#         self.assertEqual(Article.objects.count(), 5)
#
#         response = self.client.post(reverse('blog:article_delete',
#                                     kwargs={'slug': self.articles[0].slug}))
#         self.assertEqual(response.status_code, 403)
#         self.assertEqual(response.content, b'<h1>403 Forbidden</h1>')


# class ArticleUpdateViewTest(TestCase):
#     """
#     Test to check if the article create view works as required.
#     """
#     def setUp(self):
#         """
#         Model mommy creates an article.
#
#         :return: an article
#         """
#         self.client = Client()
#         self.author = mommy.make(User)
#         self.test_user1 = User.objects.create_user(username='testuser1',
#                                                    password='1X<ISRUkw+tuK')
#         self.test_user1.save()
#         self.article = mommy.make(Article, author=self.test_user1)
#
#     def test_redirect_if_not_logged_in(self):
#         response = self.client.get(reverse("article:article_update",
#                                            kwargs={'slug': self.article.slug}))
#         self.assertEqual(response.status_code, 302)
#         #self.assertRedirects(response, f"account/login/?next=/article/{self.article.slug}/update/")
#
#     def test_logged_in_uses_correct_template(self):
#         self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(reverse('article:article_update',
#                                            kwargs={'slug': self.article.slug}))
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertTemplateUsed(response, "article/article_create_form.html")
#
#     def test_update_article(self):
#         """
#         Author has to be logged in before he/she can update his or article.
#
#         When the author is logged, if he/she goes to the article he/she wants
#         to update details page.
#
#         Once he lands on the update page, he can only update, the article's
#         category, title, body and image fields.
#         After the update, check if the fields were update with the new details.
#
#         :return: Assertions
#         """
#         self.client.login(username='testuser1', password='1X<ISRUkw+tuK')
#         response = self.client.get(self.article.get_absolute_url())
#
#         new_category = mommy.make(Category)
#         new_article = mommy.make(Article, category=new_category, title="Coming",
#                                  body="New is going to be awesome")
#         article = model_to_dict(new_article)
#         update_response = self.client.get(reverse('article:article_update',
#                                                   kwargs={'slug': self.article.slug}),
#                                           article)
#
#         updated_response = self.client.get(self.article.get_absolute_url())
#         self.assertEqual(updated_response.context['article'].category,
#                          new_article.category)
#         # self.assertEqual(response.context['article'].slug, art.slug)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(str(response.context['user']), 'testuser1')
#         self.assertTemplateUsed(response, "article/article_create_form.html")




