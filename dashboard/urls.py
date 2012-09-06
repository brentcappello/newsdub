from django.conf.urls import patterns, url
from dashboard.views import DashboardView


urlpatterns = patterns('',
       url(r'^$', DashboardView.as_view(), name='dashboard-index'),
       url(r'^profile/edit/$', 'member.views.profileedit', name="edit-profile"),
       url(r'^profile/pass/$', 'member.views.passchange', name="change-password"),
#       url(r'^profile/(?P<slug>[-\w]+)/$', 'member.views.profileedit'),
#       url(r'^profile/$', ProfileView.as_view(), name="edit-profile"),
       )