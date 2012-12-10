from django.forms import ModelForm
from django.forms.fields import MultipleChoiceField
from django.forms.widgets import CheckboxSelectMultiple, TextInput, FileInput
from django.forms import ModelChoiceField

from newsscrape.models import Article

class ArticleForm(ModelForm):
    class Meta:
        model = Article
#        exclude = ('url', 'title', 'thumbnail', 'news_website', 'descriptuion', )
        fields = ('newsletters',)
        widgets = {
            'newsletters': CheckboxSelectMultiple(),
        }