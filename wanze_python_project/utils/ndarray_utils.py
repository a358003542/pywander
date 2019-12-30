#!/usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np
import pandas as pd
from collections import Iterable


def to_ndarray(pyobj, dtype=None):
    """
    将一个可迭代的python对象转变成为numpy的ndarray对象
    """
    if not isinstance(pyobj, Iterable):
        raise TypeError('it is not a iterable object')

    if isinstance(pyobj, np.ndarray):
        return pyobj

    if dtype is not None:
        return np.array(pyobj, dtype)
    else:
        return np.array(pyobj)


def mean(obj):
    """
    计算均值
    """
    obj = to_ndarray(obj)
    return obj.mean()


def median(obj, axis=None):
    """
    计算中位数
    """
    obj = to_ndarray(obj)
    return np.median(obj, axis=axis)


from collections import Counter


def mode(obj):
    """
    计算众数，支持最大相同记数返回
    """

    c = Counter(obj)

    most = 0
    first = True
    for k, v in c.most_common():
        if first:
            most = v
            first = False
            yield k
        else:
            if most == v:
                yield k
            else:
                break


def quantile(obj, seq=None):
    """
    计算分位数
    """
    obj = to_ndarray(obj)

    if seq is None:
        seq = range(0, 101, 25)

    res = pd.Series(np.percentile(obj, seq), index=seq)
    return res


def pvariance(obj):
    """
    计算总体方差
    """
    obj = to_ndarray(obj)

    return np.var(obj)


def pstd_deviation(obj):
    """
    计算总体标准差
    """
    obj = to_ndarray(obj)

    return np.std(obj)


def variance(obj):
    """
    计算样本方差
    """
    obj = to_ndarray(obj)

    return np.var(obj, ddof=1)


def std_deviation(obj):
    """
    计算样本标准差
    :param obj:
    :return:
    """
    obj = to_ndarray(obj)

    return np.std(obj, ddof=1)


def permutation(n, k):
    """
    排列数 n!(n-k)!
    :param n:
    :param k:
    :return:
    """
    from scipy.special import perm
    return perm(n, k, exact=True)


def combination(n, k):
    """
    组合数 n!/k!(n-k)!
    :param n:
    :param k:
    :return:
    """
    from scipy.special import comb
    return comb(n, k, exact=True)


def n_choose_k(n, k, order=None):
    """
    n个元素选择k个
    :param n:
    :param k:
    :param order: 默认为None，也就是组合数，其他输入值将进行bool处理，获得True之后返回排列数。
    :return:
    """
    if order is None or not bool(order):
        return combination(n, k)
    elif bool(order):
        return permutation(n, k)
