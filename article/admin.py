from article.models import Newsletter, Post
from django.contrib import admin

class NewsletterAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Newsletter, NewsletterAdmin)
admin.site.register(Post, PostAdmin)