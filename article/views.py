from dashboard.views import LoginRequiredMixin
from article.models import Post
from article.forms import PostForm, NewsletterForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User



def post_create(request, template_name='article/post_form.html'):
    form = PostForm(request.POST or None, request=request)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        form.save_m2m()
        #        msg = "Article saved successfully"
        #        messages.success(request, msg, fail_silently=True)
        return redirect('post_list')
    return render(request, template_name, {'form': form,})

def newsletter_create(request, template_name='article/newsletter_form.html'):
    form = NewsletterForm(request.POST or None)
    if form.is_valid():
        newsletter = form.save(commit=False)
        newsletter.created_by = request.user
        newsletter.save()
        #        msg = "Article saved successfully"
        #        messages.success(request, msg, fail_silently=True)
        return redirect('post_list')
    return render(request, template_name, {'form': form,})


#This is the old way of doing it... Yet still effective and proper
#def post_create(request):
#    form = PostForm(request.POST or None)
#    if form.is_valid():
#        article = form.save(commit=False)
#        article.author = request.user
#        article.save()
#        form.save_m2m()
##        msg = "Article saved successfully"
##        messages.success(request, msg, fail_silently=True)
#
#        return HttpResponseRedirect('/dashboard/') # Redirect after POST
#    else:
#        form = PostForm() # An unbound form
#
#    return render(request, 'article/post_form.html', {
#        'form': form,
#        })


class PostListView(LoginRequiredMixin, ListView):
    template_name = 'article/post_list.html'

    def get_queryset(self):
        self.authorpost = Post.objects.filter(author=self.request.user)
        return self.authorpost

    def get_context_data(self, *args, **kwargs):
        context = super(PostListView, self).get_context_data(*args, **kwargs)
        context['post_list'] = self.authorpost
        return context


class PostDetailView(LoginRequiredMixin, ListView):
    template_name = 'article/post_detail.html'
    model = Post

class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/post_update.html'
    model = Post
    form_class = PostForm

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')


