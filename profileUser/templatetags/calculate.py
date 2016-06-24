from django import template
from datetime import date

register = template.Library()


@register.filter(name='getAge')
def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))
