#!/usr/bin/env python
# -*-coding:utf-8-*-

"""

快速排序

"""


def quick_sort2(seq):
    """
    10000 的随机数列表排序：
    select_sort use time 3.0919713973999023
    quick sort use time 0.024930477142333984

    :param seq:
    :return:
    """
    if len(seq) < 2:
        return seq
    else:
        pivot = seq[0]

        less_part = [i for i in seq[1:] if i <= pivot]

        greater_part = [i for i in seq[1:] if i > pivot]

        return quick_sort(less_part) + [pivot] + quick_sort(greater_part)




import random
def quick_sort(seq):
    """

    1000000 个随机数列表
    quick_sort use time 6.718560695648193
    quick_sort2 use time 6.613989353179932

    经过测试取中间的值作为基准值不一定是最好的情况，随机取值一定保证比取第一个情况要好。
    但是也没好多少，但总的来说随机选择基准值更符合理论情况。

    :param seq:
    :return:
    """
    if len(seq) < 2:
        return seq
    else:
        pivot_index = random.randint(0, len(seq)-1)

        pivot = seq[pivot_index]

        less_part = [i for i in seq[:pivot_index] + seq[pivot_index+1:] if i <= pivot]

        greater_part = [i for i in seq[:pivot_index] + seq[pivot_index+1:] if i > pivot]

        return quick_sort(less_part) + [pivot] + quick_sort(greater_part)