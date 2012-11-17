from newsscrape.models import Article, NewsWebsite
from django.views.generic import TemplateView, ListView, DetailView

class ArticleListView(ListView):
    context_object_name = "newsroom_article_list"
    template_name = "newsscrape/newsroom_article_list.html"
    queryset = Article.objects.all()

class ArticleDetailView(DetailView):
    context_object_name = 'newsroom_article_detail'
    template_name = 'newsscrape/newsroom_article_detail.html'
    queryset = Article.objects.all()
