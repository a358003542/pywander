#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
为本模块其他内容调用的一般性函数
"""

import os
import sys
import logging
import ast

from .compat import ispy2, ispy3, reduce, basestring
from .exceptions import NotIntegerError, OutOfRangeError

logger = logging.getLogger(__name__)


def is_even(n):
    '''is this number is even, required input n is a integer.

>>> is_even(0)
True
>>> is_even(-1)
False
>>> is_even(-2)
True

    '''
    if not isinstance(n, int):
        raise NotIntegerError

    if n % 2 == 0:
        return True
    else:
        return False


def is_odd(n):
    '''is this number is odd, required input n is a integer.'''
    return not is_even(n)


def humanize_bytes(n, precision=1):
    # Author: Doug Latornell
    # Licence: MIT
    # URL: http://code.activestate.com/recipes/577081/
    """Return a humanized string representation of a number of bytes.

>>> humanize_bytes(1)
'1 B'
>>> humanize_bytes(1024)
'1.0 KiB'
>>> humanize_bytes(1024 * 123)
'123.0 KiB'
>>> humanize_bytes(1024 * 12342)
'12.1 MiB'
>>> humanize_bytes(1024 * 12342, 2)
'12.05 MiB'
>>> humanize_bytes(1024 * 1234, 2)
'1.21 MiB'
>>> humanize_bytes(1024 * 1234 * 1111, 2)
'1.31 GiB'
>>> humanize_bytes(1024 * 1234 * 1111 * 1024)
'1.3 TiB'
>>>

    """
    abbrevs = [
        (1 << 80, 'YiB'),
        (1 << 70, 'ZiB'),
        (1 << 60, 'EiB'),
        (1 << 50, 'PiB'),
        (1 << 40, 'TiB'),
        (1 << 30, 'GiB'),
        (1 << 20, 'MiB'),
        (1 << 10, 'KiB'),
        (1, 'B')
    ]

    if n == 1:
        return '1 B'

    for factor, suffix in abbrevs:
        if n >= factor:
            break

    return '%.*f %s' % (precision, n / factor, suffix)


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


def del_list(lst, indexs):
    '''
    del list base a index list

>>> del_list([0,1,2,3,4,5],[2,3])
[0, 1, 4, 5]
>>> lst = list(range(6))
>>> lst
[0, 1, 2, 3, 4, 5]
>>> del_list(lst,[2,3])
[0, 1, 4, 5]
>>> lst
[0, 1, 4, 5]
>>> del_list(lst,[0,2])
[1, 5]
>>> lst
[1, 5]

    '''
    count = 0
    for index in sorted(indexs):
        index = index - count
        del lst[index]
        count += 1
    return lst


def group_list(lst, n=1):
    '''
    group a list, in some case, it is maybe useful.

>>> list(group_list(list(range(10)),0))
Traceback (most recent call last):
AssertionError
>>> list(group_list(list(range(10)),1))
[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
>>> list(group_list(list(range(10)),2))
[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
>>> list(group_list(list(range(10)),3))
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
>>> list(group_list(list(range(10)),4))
[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

    '''
    assert n > 0
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def beep(a, b):
    '''make a sound , ref:\
     http://stackoverflow.com/questions/16573051/python-sound-alarm-when-code-finishes
    you need install  ``apt-get install sox``

    :param a: frenquency
    :param b: duration

    create a background thread,so this function does not block the main program
    '''
    if sys.platform == "win32":
        import winsound

        def _beep(a, b):
            winsound.Beep(a, b * 1000)
    elif sys.platform == 'linux':
        def _beep(a, b):
            os.system(
                'play --no-show-progress --null \
                --channels 1 synth {0} sine {1}'.format(b, float(a)))
    from threading import Thread
    thread = Thread(target=_beep, args=(a, b))
    thread.daemon = True
    thread.start()


def str2pyobj(val):
    """
    basestring to python obj or not changed
    :param val:
    :return:
    """

    try:
        val = ast.literal_eval(val)
    except Exception:
        pass
    return val


def str2num(val):
    '''
    str to int or float or raise a Exception. in some case maybe you just want
    to do some number type transform.
    '''
    assert isinstance(val, basestring)
    try:
        return int(val)
    except ValueError:
        try:
            return float(val)
        except Exception as e:
            raise e


def flatten(inlst):
    '''
    将 **多层** 列表或元组变成一维 **列表**

        >>> flatten((1,2,(3,4),((5,6))))
        [1, 2, 3, 4, 5, 6]
        >>> flatten([[1,2,3],[[4,5],[6]]])
        [1, 2, 3, 4, 5, 6]

    '''
    lst = []
    for x in inlst:
        if not isinstance(x, (list, tuple)):
            lst.append(x)
        else:
            lst += flatten(x)
    return lst


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


from collections import ChainMap


def merge_dict_proxy(*args):
    """
    实际返回一个ChainMap对象，其将多个字典值合并，但实际相当于一个代理引用的都是字典的原值
    """
    for arg in args:
        assert isinstance(arg, dict)

    return ChainMap(*args)


def is_prime(n):
    '''test input integer n is a prime.
>>> is_prime(0)
False
>>> is_prime(-5)
False
>>> is_prime(-5.2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "__init__.py", line 12, in is_prime
    raise NotIntegerError
NotIntegerError
>>> is_prime(5)
True
>>> is_prime(123)
False

    '''
    if not isinstance(n, int):
        raise NotIntegerError

    if n == 2:
        return True
    elif n < 2 or not n & 1:
        return False
    for x in range(3, int(n ** 0.5) + 1, 2):
        if n % x == 0:
            return False
    return True


def gen_prime(n):
    '''到第n个的所有素数的生成器函数'''
    count = 0
    x = 1
    while count < n:
        if is_prime(x):
            count += 1
            yield x
        x += 1


def gen2_prime(n):
    '''到小于某个数n的所有素数的生成器函数'''
    for x in range(n):
        if is_prime(x):
            yield x


def last_gen(genobj):
    """
    迭代一个生成器对象，返回最后一个元素
    :param genobj:
    :return:
    """
    for i in genobj:
        last_e = i

    return last_e


def prime(n):
    '''第n个素数 根据last_gen函数，所以integer类型不用判断了
    名字取做prime而不是index_prime是因为计数从1开始。'''
    if n <= 0:
        raise OutOfRangeError("第零个或者第负数个素数？")
    else:
        return last_gen(gen_prime(n))


################################
# 菲波那奇数列


def gen_fibonacci(n):
    '''到第n个的斐波那契数列生成器函数'''
    if not isinstance(n, int):
        raise NotIntegerError

    count = 0
    a, b = 0, 1

    while count < n:
        yield a
        a, b = b, a + b
        count += 1


def fibonacci(n):
    '''第几个斐波那契数'''
    if n <= 0:
        raise OutOfRangeError("没有零个或小于零个斐波那契数的概念那。")
    else:
        return last_gen(gen_fibonacci(n))


#############################
# 阶乘生成器 阶乘也用生成器是因为这个迭加相乘过程非常适合做成生成器
def gen_factorial(stop, start=1):
    '''start*....stop的生成器，默认start=1'''
    if not isinstance(stop, int):
        raise NotIntegerError
    if not isinstance(start, int):
        raise NotIntegerError

    count = 0
    m = start
    n = stop - start + 1
    if stop <= 0:
        raise OutOfRangeError("负数和零的阶乘没有意义")
    elif stop < start:
        raise ValueError("终值应该比初值大")
    else:
        while count < n:
            yield start
            start = start * (m + 1)
            m += 1
            count += 1


def factorial(stop, start=1):
    '''start*....stop的值，默认start=1即为stop!的值'''
    if stop <= 0:
        raise OutOfRangeError("负数和零的阶乘没有意义")
    elif stop < start:
        raise ValueError("终值应该比初值大")
    else:
        return last_gen(gen_factorial(stop, start))


##################


def sumall(*args):
    '''将所有的数字都加起来，支持多层结构。
>>> sumall(1,1,2,3,[1,2,3])
13
>>> sumall(1,1,2,3,[1,2,3],(4,5,6),[[5,5],[6]])
44
>>>
    '''
    args = flatten(args)
    return sum(args)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
