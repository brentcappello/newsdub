from dashboard.views import LoginRequiredMixin
from article.models import Post
from article.forms import PostForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, ListView
from django.http import HttpResponseRedirect




class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'article/post_form.html'
    model = Post
    form_class = PostForm

    def get_initial(self):
        self.initial.update({ 'author': self.request.user })
        return self.initial



#    def __init__(self):
#        authorz = self.request.user
#        form = PostForm( initial={'author':authorz} )

#    def author_view(self):
#        self.author = self.request.user
#        return self.author
#        form = PostForm( initial={'author':request.user} )
#
#
#
#    def get_context_data(self, *args, **kwargs):
#        context = super(PostCreateView, self).get_context_data(*args, **kwargs)
##        context['profile'] = self.author_view()
#        return context



#    def get_initial(self):
#        self.initial.update({ 'author': self.request.user })
#        return self.initial

#
#    def form_valid(self, form):
#        obj = form.save(commit=False)
#        obj.author = self.request.user
#        obj.save()
#        return HttpResponseRedirect('/')


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'article/post_list.html'
    model = Post

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['post_list'] = Post.objects.all()
        return context

class PostDetailView(LoginRequiredMixin, ListView):
    template_name = 'article/post_detail.html'
    model = Post

#    def get_context_data(self, *args, **kwargs):
#        context = super(PostDetailView, self).get_context_data(*args, **kwargs)
#        context['blog_post'] = Post.objects.all()
#        return context
