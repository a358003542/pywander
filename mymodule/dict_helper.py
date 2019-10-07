#!/usr/bin/env python
# -*-coding:utf-8-*-

from collections import ChainMap
from functools import reduce

from mymodule.compat import ispy2, ispy3


def gen_dict_strset(d):
    s = set()
    for k, v in d.items():
        item = str(k) + ':' + str(v)
        s.add(item)
    return s


def compare_dict_include(d, include=None):
    '''
    <=  compare two dict object include or contained relationship
    return True : d totally contain the include with the same content

>>> compare_dict_include({'a':1},{})
True
>>> compare_dict_include({'a':1},{'a':2})
False
>>> compare_dict_include({'a':1},{'a':1})
True
>>> compare_dict_include({'a':1,'b':2},{'a':1})
True
>>> compare_dict_include({'a':1,'b':2},{'b':2})
True
    '''
    include = include if include is not None else {}

    if include == {}:  # always True
        return True

    ds_set = gen_dict_strset(d)
    includes_set = gen_dict_strset(include)
    if includes_set.issubset(ds_set):
        return True
    else:
        return False


def check_dict_has(d, has=None):
    '''
    does the dict object has some keys

>>> check_dict_has({'a':1,'b':2},[])
True
>>> check_dict_has({'a':1,'b':2},['a'])
True
>>> check_dict_has({'a':1,'b':2},['a','c'])
False
>>> check_dict_has({'a':1,'b':2},['a','b'])
True

    '''
    has = has if has is not None else []

    if has == []:  # always True
        return True

    if set(has).issubset(set(d.keys())):
        return True
    else:
        return False


def merge_dict(*args):
    """
    将多个字典值合并，如果key相同，则以后面的为准。
    ref : http://stackoverflow.com/questions/38987/\
    how-can-i-merge-two-python-dictionaries-in-a-single-expression
    """

    def add(x, y):
        return x + y

    if ispy2:
        res = dict(reduce(add, [d.items() for d in args]))
        return res
    elif ispy3:
        res = dict(reduce(add, [list(d.items()) for d in args]))
        return res
    else:
        raise Exception('unbelievable')


def merge_dict_proxy(*args):
    """
    实际返回一个ChainMap对象，其将多个字典值合并，但实际相当于一个代理引用的都是字典的原值
    """
    for arg in args:
        assert isinstance(arg, dict)

    return ChainMap(*args)
