from django.conf.urls import patterns, url
from newsscrape.views import ArticleListView, ArticleDetailView


urlpatterns = patterns('',
    url(r'^articles/$',  ArticleListView.as_view(), name='newsroom_list'),
    url(r'^detail/(?P<pk>.*)/$', ArticleDetailView.as_view(), name='newsroom_detail')

)