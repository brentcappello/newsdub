from dashboard.views import LoginRequiredMixin
from article.models import Post, Newsletter, Publication
from article.forms import PostForm, NewsletterForm, PostFormUpdate, PublicationForm
from django.views.generic.edit import ModelFormMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.http import Http404
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# OK this still confuses me how this works but my million
# other tries did not
@login_required
def post_create(request, template_name='article/post_form.html'):
    the_creator = request.user

    if request.POST:
        form = PostForm(the_creator, request.POST, request.FILES)
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
def publication_create(request, template_name='article/publication_form.html'):
    form = PublicationForm(request.POST or None)
    if form.is_valid():
        publication = form.save(commit=False)
        publication.created_by = request.user
        publication.save()
        #        msg = "Article saved successfully"
        #        messages.success(request, msg, fail_silently=True)
        return redirect('post_list')
    return render(request, template_name, {'form': form,})

@login_required
def newsletter_create(request, template_name='article/newsletter_form.html'):
    form = NewsletterForm(request.POST or None)
    form.fields['publication'].queryset = Publication.objects.filter(created_by=request.user)
    if form.is_valid():
        newsletter = form.save(commit=False)
        newsletter.created_by = request.user
        newsletter.save()
        form.save_m2m()
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

class PublicationListView(LoginRequiredMixin, ListView):
    template_name = 'article/publication_list.html'

    def get_queryset(self):
        self.authorpost = Publication.objects.filter(created_by=self.request.user)
        return self.authorpost

    def get_context_data(self, *args, **kwargs):
        context = super(PublicationListView, self).get_context_data(*args, **kwargs)
        context['publication_list'] = self.authorpost
        return context

@login_required
def issue_list(request, slug):
    issue = get_object_or_404(Publication, slug=slug, created_by=request.user)
    return render(request, 'article/issue_list.html', {
        'object_list': issue.newsletter_set.all(),
        })

class NewsletterListView(LoginRequiredMixin, ListView):
    template_name = 'article/newsletter_list.html'

    def get_queryset(self):
        self.authorpost = Newsletter.objects.filter(created_by=self.request.user)
        return self.authorpost

    def get_context_data(self, *args, **kwargs):
        context = super(NewsletterListView, self).get_context_data(*args, **kwargs)
        context['newsletter_list'] = self.authorpost
        return context


#I probably could have done this differently with CBGV
@login_required
def newsletter_tabular(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug, created_by=request.user)
    return render(request, 'article/newsletter_post_tabular.html', {
        'object_list': newsletter.post_set.all(),
        'newsletter': newsletter,
        })

@login_required
def newsletter_grid(request, slug):
    newsletter = get_object_or_404(Newsletter, slug=slug, created_by=request.user)
    return render(request, 'article/newsletter_post_grid.html', {
        'object_list': newsletter.post_set.all(),
        'newsletter': newsletter,
        })

def newsletter_pub(request, slug, author):
    theauthor = User.objects.get(username=author).id
    newsletter = get_object_or_404(Newsletter, slug=slug, created_by=theauthor)
    return render(request, 'article/newsletter_post_pub.html', {
        'object_list': newsletter.post_set.all(),
        'newsletter': newsletter,
        })


#class PostDetailViewPub(DetailView):
#    template_name = 'article/post_detail_pub.html'
#    model = Post

def article_pub(request, slug, author):
    theauthor = User.objects.get(username=author).id
    post = get_object_or_404(Post, slug=slug, author=theauthor)
    return render(request, 'article/post_detail_pub.html', {
        'object': post,
        })

#class NewsletterPostListView(LoginRequiredMixin, ListView):
#    template_name = 'article/newsletter_post_tabular.html'
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

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
#    success_url = reverse_lazy('post_list')

    def get_success_url(self):
        return self.request.POST.get('path')




#class NewsletterPostListView(LoginRequiredMixin, ListView):
#    template_name = 'article/newsletter_post_tabular.html'
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
    success_url = reverse_lazy('newsletter_list')
    form_class = NewsletterForm

    def get_form(self, form_class):
        form = super(NewsletterUpdateView,self).get_form(form_class) #instantiate using parent
        form.fields['publication'].queryset = Publication.objects.filter(created_by=self.request.user)
        return form


class NewsletterDeleteView(LoginRequiredMixin, DeleteView):
    model = Newsletter
    success_url = reverse_lazy('newsletter_list')


#class PostDetailView(LoginRequiredMixin, ListView):
#    template_name = 'article/post_detail.html'
#    model = Post



class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article/post_update.html'
    model = Post
    form_class = PostFormUpdate

    def get_form(self, form_class):
        form = super(PostUpdateView,self).get_form(form_class) #instantiate using parent
        form.fields['newsletters'].queryset = Newsletter.objects.filter(created_by=self.request.user)
        return form