# Core Django imports.
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import (
    CreateView,
    ListView,
)

# Blog application imports.
from blog.models.article_models import Article
from blog.models.comment_models import Comment
from blog.forms.blog.comment_forms import CommentForm


class CommentCreateView(CreateView):
    form_class = CommentForm

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.article = get_object_or_404(Article,
                                            slug=self.kwargs.get('slug'))
        comment.save()
        messages.success(self.request, "Comment Added successfully")
        return redirect('blog:article_comments', comment.article.slug)


class ArticleCommentList(ListView):
    context_object_name = "comments"
    paginate_by = 10
    template_name = "blog/comment/article_comments.html"

    def get_queryset(self):
        article = get_object_or_404(Article, slug=self.kwargs.get('slug'))
        queryset = Comment.objects.filter(article=article)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ArticleCommentList, self).get_context_data(**kwargs)
        context['article'] = get_object_or_404(Article,
                                               slug=self.kwargs.get('slug'))
        context['comment_form'] = CommentForm
        return context

