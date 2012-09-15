from dashboard.views import LoginRequiredMixin
from article.models import Post, Newsletter
from article.forms import PostForm, NewsletterForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# OK this still confuses me how this works but my million
# other tries did not
@login_required
def post_create(request, template_name='article/post_form.html'):
    the_creator = request.user

    if request.POST:
        form = PostForm(the_creator, request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            form.save_m2m()
            #        msg = "Article saved successfully"
            #        messages.success(request, msg, fail_silently=True)
            return redirect('post_list')
    else:
        form = PostForm(the_creator)
    return render(request, template_name, {'form': form,})

#def post_create(request):
#    if request.method == 'POST':
#        form = PostForm(request.POST)
#        if form.is_valid():
#            article = form.save(commit=False)
#            article.author = request.user
#            article.save()
#            form.save_m2m()
#            #        msg = "Article saved successfully"
#            #        messages.success(request, msg, fail_silently=True)
#            return redirect('post_list')
#    else:
#        form = PostForm(newsletter_user)
#    return render(request, 'article/post_form.html', {'form': form,})
@login_required
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




class NewsletterListView(LoginRequiredMixin, ListView):
    template_name = 'article/newsletter_list.html'

    def get_queryset(self):
        self.authorpost = Newsletter.objects.filter(created_by=self.request.user)
        return self.authorpost

    def get_context_data(self, *args, **kwargs):
        context = super(NewsletterListView, self).get_context_data(*args, **kwargs)
        context['newsletter_list'] = self.authorpost
        return context

#I probably could have easily done this in a CBGV
def newsletter_detail(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug)
    return render(request, 'article/newsletter_post_list.html', {
        'object_list': newsletter.post_set.all(),
        'newsletter': newsletter,
        })


#class NewsletterPostListView(LoginRequiredMixin, ListView):
#    template_name = 'article/newsletter_post_list.html'
#
##    def newsletter_view(self):
##        self.newsletter = get_object_or_404(Newsletter, slug=slug)
##        return self.member
#    def get_queryset(self):
#        self.newsletter = get_object_or_404(Newsletter, slug=self.slug)
#        return models.Article.public.language(self.args[1]).filter(categories=self.category)
#
#    def get_context_data(self, *args, **kwargs):
#        self.newsletters = get_object_or_404(Newsletter, slug=slug)
#        context = super(NewsletterPostListView, self).get_context_data(*args, **kwargs)
#        return context







#class NewsletterPostListView(LoginRequiredMixin, ListView):
#    template_name = 'article/newsletter_post_list.html'
#
#    def get_queryset(self):
#        self.newsletter_articles = Post.objects.filter(newsletters=self.newsletter_articles)
#        return self.newsletter_articles
#
#    def get_context_data(self, *args, **kwargs):
#        context = super(NewsletterPostListView, self).get_context_data(*args, **kwargs)
#        context['newsletter_post_list'] = self.newsletter_articles
#        return context

class NewsletterUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/newsletter_update.html'
    model = Newsletter
    form_class = NewsletterForm

class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter_list')

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


