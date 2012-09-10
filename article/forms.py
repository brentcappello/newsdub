from django.forms import ModelForm
from django.contrib.auth.models import User
from article.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ('author', 'publish', 'created_at',)

#    def __init__(self, *args, **kwargs):
#        self.author = kwargs['initial']['author']
#        super(PostForm, self).__init__(*args, **kwargs)
#
#    def save(self, commit=True):
#        obj = super(PostForm, self).save(False)
#        obj.author = self.author
#        commit and obj.save()
#        return obj

#class PostListForm(ModelForm):
#    class Meta:
#        model = Post
#        fields = ('author', 'title', 'status', 'publish')