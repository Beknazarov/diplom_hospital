from django import template

register = template.Library()


@register.filter(name='zip')
def zip_lists(a, b):
    return zip(a, b)


@register.filter(name='cut_desc')
def cut_word(a):
    return a[:340]


@register.filter(name='cut_title')
def cut_word(a):
    return a[:50]


@register.filter(name='cut_title2')
def cut_word(a):
    return a[:200]

