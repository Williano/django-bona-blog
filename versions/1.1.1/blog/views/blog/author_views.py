# Core Django imports.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
)

# Blog application imports.
from blog.models.article_models import Article


class AuthorArticlesListView(ListView):
    model = Article
    paginate_by = 12
    context_object_name = 'articles'
    template_name = 'blog/authors/author_articles.html'

    def get_queryset(self):
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        return Article.objects.filter(author=author, status=Article.PUBLISHED, deleted=False)

    def get_context_data(self, **kwargs):
        context = super(AuthorArticlesListView, self).get_context_data(**kwargs)
        author = get_object_or_404(User, username=self.kwargs.get('username'))
        context['author'] = author
        return context


class AuthorsListView(ListView):
    model = User
    paginate_by = 12
    context_object_name = 'authors'
    template_name = 'blog/authors/authors_list.html'

    def get_queryset(self):
        return User.objects.all().order_by('-date_joined')
