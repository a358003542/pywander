#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

logger = logging.getLogger(__name__)


def get_related_value(d, item):
    if item in d:
        return d[item]

    if item in d.values():
        return item

    raise ValueError("Can not found the related value.")


def remove_dict_key(d, keys):
    """
    就地删除某个字典的key
    :param d:
    :param key:
    :return:
    """
    if isinstance(keys, str):
        keys = [keys]

    for key in keys:
        try:
            del d[key]
        except KeyError:
            pass
            # logger.warning('there is not {0} key.'.format(key))
    return d


def remove_dict_key_safely(d, key):
    new_d = d.copy()
    try:
        del new_d[key]
    except KeyError:
        pass
        # logger.warning('there is not {0} key.'.format(key))
    return new_d
