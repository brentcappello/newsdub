from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def is_active(current_path, urls):
    if current_path in (reverse(url) for url in urls.split()):
        return "active"
    return ''

@register.simple_tag
def is_account(current_path):
    choices = ['/dashboard/account', '/coolsomething']
    for choice in choices:
        if choice in current_path:
            return "active"
    return ''

@register.simple_tag
def is_newsletter(current_path):
    choices = ['/newsletters/', 'cool']
    for choice in choices:
        if choice in current_path:
            return "active"
    return ''