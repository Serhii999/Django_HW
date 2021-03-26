from django import template
from random import randint, choice
from string import ascii_letters

register = template.Library()


@register.simple_tag
def random_id():
    return randint(1, 100000)


@register.simple_tag
def random_slug():
    return ''.join(choice(ascii_letters) for string in range(randint(5, 10)))