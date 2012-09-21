from django.db import models
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User

from taggit.managers import TaggableManager
import os


class Newsletter(models.Model):
    STATUS_CHOICES = (
        (1, 'Draft'),
        (2, 'Public')
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    created_by = models.ForeignKey(User)
    publish = models.DateTimeField(default=datetime.now)
    created_at = models.DateTimeField(default=datetime.now)
    status = models.IntegerField(choices=STATUS_CHOICES, default=2)

    class Meta:
        ordering = ('-publish',)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return self.slug


def get_image_path(instance, filename):
    return "user_{id}/{file}".format(id=instance.author.id, file=filename)

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
    newsletters = models.ManyToManyField(Newsletter, help_text='good job')
    image = models.ImageField(upload_to=get_image_path, blank=True)
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
        return ('post_detail', None, {
#            'author': self.author.username,
#            'year': self.publish.year,
#            'month': '%02d' % self.publish.month,
            'slug': self.slug
        })





