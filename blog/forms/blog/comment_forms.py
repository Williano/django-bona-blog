# Core Django imports.
from django.forms import ModelForm, TextInput, EmailInput, Textarea

# Blog application imports.
from blog.models.comment_models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', ]
        widgets = {
            'name': TextInput(attrs={'aria-required': "true",
                                     'name': "contact-form-name",
                                     'class': "form-control",
                                     'placeholder': "Enter your name",
                                     'aria-invalid': "true"
                                     }),

            'email': EmailInput(attrs={'aria-required': "true",
                                       'name': "contact-form-email",
                                       'class': "form-control",
                                       'placeholder': "Enter your email",
                                       'aria-invalid': "true",
                                       }),

            'comment': Textarea(attrs={'name': "contact-form-message",
                                       'rows': "2",
                                       'class': "text-area-messge form-control",
                                       'placeholder': "Enter your comment",
                                       'aria - required': "true",
                                       'aria - invalid': "false"
                                       }),
        }

