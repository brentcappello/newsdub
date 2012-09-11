from article.models import Newsletter
from django.contrib import admin

class NewsletterAdmin(admin.ModelAdmin):
    pass

admin.site.register(Newsletter, NewsletterAdmin)