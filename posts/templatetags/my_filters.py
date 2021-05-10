from django import template

register = template.Library()


@register.simple_tag
def my_range(n):
    return range(n)
#
# @register.filter
# def to_upper(value):
#     return value[::-1]
#
#
# @register.filter
# def cut(value, n):
#     return value[:n]

