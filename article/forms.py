from django.forms import ModelForm
from django.contrib.auth.models import User
from article.models import Post, Newsletter
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple, TextInput
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
            'newsletters': CheckboxSelectMultiple(),
            'title': TextInput(attrs={'onkeyup':'updateslug()'})
        }

    #this took fucking foooooorever to figure out - I still not sure how it works lol.
    def __init__(self, created_by=None, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['newsletters'].queryset = Newsletter.objects.filter(created_by=created_by)



class PostFormUpdate(ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'publish', 'created_at',)
        widgets = {
            'newsletters': CheckboxSelectMultiple(),
            'title': TextInput(attrs={'onkeyup':'updateslug()'})
        }
