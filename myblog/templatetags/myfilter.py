#!/usr/bin/env python
# -*- coding: utf-8 -*-
# by qiuyinjia

from django import template

register = template.Library()


# @register.filter(name='key')
def key(d, key_name):
        try:
                value = d[str(key_name)]
        except KeyError:
                value = 0
        return value
register.filter('key', key)
