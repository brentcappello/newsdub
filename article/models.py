from django.db import models
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

class Post(models.Model):
    """Post Model."""
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(User, related_name="added_posts")
#    creator_ip = models.IPAddressField(blank=True)
    body = models.TextField()
    tease = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)
    allow_comments = models.BooleanField(default=True)
    publish = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    tags = TaggableManager()
    #    updated_at = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-publish',)
        get_latest_by = 'publish'

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blog_post', None, {
#            'author': self.author.username,
#            'year': self.publish.year,
#            'month': '%02d' % self.publish.month,
            'slug': self.slug
        })




