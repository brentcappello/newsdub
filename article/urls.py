from django.conf.urls import patterns, url, include
from django.views.generic import DetailView
from article.models import Post
from article.views import *


urlpatterns = patterns('',
    url(r'^create/$', 'article.views.newsletter_create', name='newlsetter_create'),
#    url(r'^newsletters/$', NewsletterListView.as_view(), name='newsletter_list'),
    url(r'^update_news/(?P<slug>.*)/$', NewsletterUpdateView.as_view(), name="newsletter_update",),
    url(r'^delete_newsletter/(?P<slug>.*)/$', NewsletterDeleteView.as_view(), name="newsletter_delete",),
#    url(r'^newsletter/(?P<slug>.*)/$', NewsletterPostListView.as_view(), name='newsletter_post_list'),


    url(r'^add/$', 'article.views.post_create', name='post'),
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^update/(?P<slug>.*)/$', PostUpdateView.as_view(), name="post_update",),
    url(r'^detail/(?P<slug>.*)/$', DetailView.as_view(model=Post, context_object_name="post_detail",), name='post_detail'),
    url(r'^delete/(?P<slug>.*)/$', PostDeleteView.as_view(), name="post_delete",),

#    url(r'^list/$', ListView.as_view(model=Post, context_object_name="post_list",)),
#    url(r'^add/$', CreateView.as_view(model=Post, context_object_name="add-article",)),

)

urlpatterns += patterns('article.views',
    url(r'^newsletters/$', NewsletterListView.as_view(), name='newsletter_list'),
    url(r'^newsletters/(?P<slug>.*)/$', 'newsletter_detail', name='newsletter_detail' ),
#    url(r'^newsletters/(?P<slug>.*)/$', NewsletterArticleListView.as_view(), name='newsletter_post_list'),
)