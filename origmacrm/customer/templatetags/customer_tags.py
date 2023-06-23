from django import template

from ..models import Customer

register = template.Library()


@register.filter
def industry(query):
    for choice in Customer.INDUSTRY_OPTIONS:
        if choice[0] == query:
            return choice[1]
    return ""
