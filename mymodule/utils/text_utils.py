#!/usr/bin/env python
# -*- coding: utf-8 -*-


import re


def multi_delimiter_split(string, delimiters='', split_whitespace=True,
                          remove_whitespace=True):
    """
    多个分隔符分割字符串，

    delimiters = ';,'
    split_whitespace 是否加上按照空白分割   默认是按照空白分割
    remove_whitespace 是否移除分隔符两边多余的空白字符 默认移除


    """
    expr_one = '\s' if split_whitespace else ''

    expr = '[{0}{1}]'.format(delimiters, expr_one)

    if remove_whitespace:
        expr = '\s*' + expr + '\s*'

    res = re.split(expr, string)

    return res
