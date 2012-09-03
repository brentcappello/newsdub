from django.conf.urls import patterns, url
from dashboard.views import DashboardView
from member.views import ProfileView


urlpatterns = patterns('',
       url(r'^$', DashboardView.as_view(), name='dashboard-index'),
       url(r'^profile/$', ProfileView.as_view(), name="edit-profile"),
       )