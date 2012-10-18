from django.conf.urls import patterns, url, include
from django.views.generic import DetailView
from article.models import Post
from article.views import *


urlpatterns = patterns('',
    url(r'^create/$', 'article.views.publication_create', name='publication_create'),
    url(r'^create/issue/$', 'article.views.newsletter_create', name='newlsetter_create'),
#    url(r'^newsletters/$', NewsletterListView.as_view(), name='newsletter_list'),
    url(r'^update_news/(?P<slug>.*)/$', NewsletterUpdateView.as_view(), name="newsletter_update",),
    url(r'^delete_newsletter/(?P<slug>.*)/$', NewsletterDeleteView.as_view(), name="newsletter_delete",),
#    url(r'^newsletter/(?P<slug>.*)/$', NewsletterPostListView.as_view(), name='newsletter_post_list'),

    url(r'^article/add/$', 'article.views.post_create', name='post'),
    url(r'^articles/$', PostListView.as_view(), name='post_list'),
    url(r'^article/update/(?P<slug>.*)/$', PostUpdateView.as_view(), name="post_update",),
    #I had a bug here when I added the author to the URL and added the class meta author to the model. For some
    # reason I was unable to view some newsletters without throwing an error, (?P<author>.*)/
    url(r'^article/pub/(?P<author>.*)/(?P<slug>.*)/$', 'article.views.article_pub', name='post_detail_pub'),
    url(r'^article/(?P<slug>.*)/$', DetailView.as_view(model=Post, context_object_name="post_detail",), name='post_detail'),
    url(r'^delete_article/(?P<slug>.*)/$', PostDeleteView.as_view(), name="post_delete"),

#    url(r'^list/$', ListView.as_view(model=Post, context_object_name="post_list",)),
#    url(r'^add/$', CreateView.as_view(model=Post, context_object_name="add-article",)),
)

urlpatterns += patterns('article.views',
    url(r'^publications/$', PublicationListView.as_view(), name='publication_list'),
    url(r'^issues/(?P<slug>.*)/$', 'issue_list', name='issue_list' ),
)


urlpatterns += patterns('article.views',
    url(r'^$', NewsletterListView.as_view(), name='newsletter_list'),
    url(r'^tabular/(?P<slug>.*)/$', 'newsletter_tabular', name='newsletter_tabular' ),
    url(r'^grid/(?P<slug>.*)/$', 'newsletter_grid', name='newsletter_grid' ),
    url(r'^pub/(?P<author>.*)/(?P<slug>.*)/$', 'newsletter_pub', name='newsletter_pub' ), #public facing view
#    url(r'^article/pub/(?P<author>.*)/(?P<slug>.*)/$', 'article_pub', name='post_detail_pub'),
#    url(r'^newsletters/(?P<slug>.*)/$', NewsletterArticleListView.as_view(), name='newsletter_post_list'),
)