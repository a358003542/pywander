#!/usr/bin/env python
# -*-coding:utf-8-*-

"""

这里放着很多和项目相关的唯一性标识id生成函数，慢慢都应该在这里汇总，规范起来。

"""
from collections import OrderedDict
from hashlib import md5
from urllib.parse import urlencode

from utils import remove_dict_key


def build_query_id(base_url, params, remove_keys=None):
    """
    针对某个网络上的url请求，get请求，加上参数，最后返回什么结果的 唯一id标识
    """
    data = params.copy()

    if remove_keys:
        remove_dict_key(data, remove_keys)

    data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))

    url = "{base_url}?{ps}".format(
        base_url=base_url,
        ps=urlencode(data)
    )
    query_id = md5(url.encode()).hexdigest()
    return query_id
