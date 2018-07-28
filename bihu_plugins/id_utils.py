#!/usr/bin/env python
# -*-coding:utf-8-*-


from bihu.utils import remove_dict_key
from collections import OrderedDict
from hashlib import md5
from urllib.parse import urlencode



def build_operation_id(source, operation, params, remove_keys=None):
    """
    某些缓存需求用如下方式来定制可能会更方便一些：
    针对某个源进行了某个操作 挂上什么参数 然后对应 什么结果
    source operation 参数 对应同样的结果
    """
    data = params.copy()

    if remove_keys:
        remove_dict_key(data, remove_keys)

    data = OrderedDict(sorted(data.items(), key=lambda t: t[0]))

    url = "{source}/{operation}?{ps}".format(
        source=source,
        operation=operation,
        ps=urlencode(data)
    )
    operation_id = md5(url.encode()).hexdigest()
    return operation_id




print('plugin id_utils loaded.')