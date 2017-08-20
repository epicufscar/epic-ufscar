import os
from django import template
register = template.Library()


@register.filter
def imagename(value):
    return os.path.basename(value.file.name)
