from django.forms import ModelForm
from django.contrib.auth.models import User
from article.models import Post, Newsletter
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple
from django.forms import ModelChoiceField

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

    #this was tricky I needed to add the kwargs.pop in order to filter the field by request.user
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(PostForm, self).__init__(**kwargs)
        self.fields['newsletters'].queryset = Newsletter.objects.filter(created_by=self.request.user)



