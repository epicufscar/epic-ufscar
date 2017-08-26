import os
from django import template
register = template.Library()


@register.filter
def imagename(value):
    return os.path.basename(value.file.name)


@register.filter
def in_workshop_groups(groups, workshop):
    return groups.filter(workshop=workshop)