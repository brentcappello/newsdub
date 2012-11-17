from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib.auth.views import password_reset, password_reset_confirm
import registration.backends.default.urls as regUrls
from member.regbackend import UserRegistrationForm
from registration.views import register
from django.conf import settings

from core.views import HomeView

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^dashboard/', include('dashboard.urls')),
    url(r'^newsletters/', include('article.urls')),
    url(r'^newsroom/', include('newsscrape.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'extra_context': {'registration_form': UserRegistrationForm()}}, name='auth_login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {"next_page": "/"}, name='auth_logout'),
    url(r'^accounts/password/reset/$', password_reset, {'email_template_name': 'email_password_reset.txt', 'subject_template_name': 'email_password_reset_title.txt', 'template_name': 'password_reset.html'}, name='password_reset'),
    url(r'^accounts/password/reset/done/$', TemplateView.as_view(template_name="password_reset_sent.html"), name='password_reset_sent'),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', password_reset_confirm, {"template_name": "password_reset_confirm.html"}, name='password_reset_confirm'),
#    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/register/$', register, {'backend': 'registration.backends.default.DefaultBackend','form_class': UserRegistrationForm}, name='registration_register'),(r'^accounts/', include(regUrls)),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
         'django.views.static.serve', {'document_root':'./newsdub/media/'}),)

