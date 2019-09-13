from django import template

register = template.Library()


@register.filter(name='sentence_case')
def sentence_case(value):
    return value.capitalize()
