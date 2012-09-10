from django.conf.urls import patterns, url, include
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from article.models import Post
from article.views import PostCreateView, PostListView


urlpatterns = patterns('',
    url(r'^add/$', PostCreateView.as_view(), name='post'),
    url(r'^list/$', PostListView.as_view(), name='post_list'),
    url(r'^update/$', UpdateView.as_view(model=Post, context_object_name="post_update",)),
    url(r'^detail/(?P<slug>.*)/$', DetailView.as_view(model=Post, context_object_name="blog_post",), name='blog_post'),
#    url(r'^detail/(?P<slug>.*)/$', PostDetailView.as_view(), name="blog_post"),
    url(r'^delete/$', DeleteView.as_view(model=Post, context_object_name="post_delete",)),

#    url(r'^list/$', ListView.as_view(model=Post, context_object_name="post_list",)),
#    url(r'^add/$', CreateView.as_view(model=Post, context_object_name="add-article",)),

)