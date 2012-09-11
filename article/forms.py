from django.forms import ModelForm
from django.contrib.auth.models import User
from article.models import Post, Newsletter
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple

class NewsletterForm(ModelForm):
    class Meta:
        model = Newsletter
        exclude = ('created_by', 'publish', 'created_at',)


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'publish', 'created_at',)
        widgets = {
            'newsletters': CheckboxSelectMultiple()
        }

