#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
重新设计，使其成为一个即使是之于scrapy这样的大型网络抓取框架，也能提供一些便捷的函数支持。

"""


from .common import to_absolute_url
from .api import Api, memorized_property

__all__ = [
    'memorized_property',
    'Api',
    'to_absolute_url'
]
