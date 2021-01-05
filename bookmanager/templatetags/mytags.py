# /usr/bin/env python3
# code: utf-8

from django import template

register = template.Library()


@register.filter(name="yourname")
def add_arg(value, arg):
    # 功能
    return "{}_{}".format(value, arg)
