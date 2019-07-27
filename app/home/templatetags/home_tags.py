from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag(name='get_conf')
def get_conf(value):
    if value in settings:
        return getattr(settings, value)
    return None
