from dashboard.views import LoginRequiredMixin
from newsscrape.models import Article, NewsWebsite
from article.models import Newsletter
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.views.generic.edit import FormMixin
from django.core.urlresolvers import reverse_lazy
from newsscrape.forms import ArticleForm
from django.http import HttpResponseForbidden

class ArticleListView(LoginRequiredMixin, ListView, FormMixin):
    context_object_name = "newsroom_article_list"
    template_name = "newsscrape/newsroom_article_list.html"
    form_class = ArticleForm
    success_url = reverse_lazy('newsroom_list')
    queryset = Article.objects.all()


    def get_context_data(self, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        form.fields['newsletters'].queryset = Newsletter.objects.filter(created_by=self.request.user)
        context = {
            'form': form
        }
        context.update(kwargs)
        return super(ArticleListView, self).get_context_data(**context)

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        if not self.request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        # record the interest using the message in form.cleaned_data
        return super(AuthorDetail, self).form_valid(form)

class ArticleDetailView(DetailView):
    context_object_name = 'newsroom_article_detail'
    template_name = 'newsscrape/newsroom_article_detail.html'
    queryset = Article.objects.all()

#def newsroom_article_pub(request, slug, author=None, layout=None):
#    layout_style = layout
#    #    theauthor = User.objects.get(username=author).id
#    post = get_object_or_404(Post, slug=slug, author=theauthor)
#    return render(request, 'article/newsroom_article_detail_pub.html', {
#        'object': post,
#        'layout' : layout_style,
#        })

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    context_object_name = 'newsroom_article_update'
    template_name = 'newsscrape/newsroom_article_update.html'
    success_url = reverse_lazy('newsroom_list')
#    queryset = Article.objects.all()
    model = Article
    form_class = ArticleForm

    def get_form(self, form_class):
        form = super(ArticleUpdateView,self).get_form(form_class) #instantiate using parent
        form.fields['newsletters'].queryset = Newsletter.objects.filter(created_by=self.request.user)
        return form


