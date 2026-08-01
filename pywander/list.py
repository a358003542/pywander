#!/usr/bin/env python
# -*-coding:utf-8-*-

from itertools import product, permutations, combinations, \
    combinations_with_replacement

from collections import UserList
from typing import List, Optional


def del_list(lst: list, indexs):
    """
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

    """
    count = 0
    for index in sorted(indexs):
        index = index - count
        del lst[index]
        count += 1
    return lst


def group_list(lst: list, n=1):
    """
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

    """
    assert n > 0
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def combine_odd_even(lst):
    """
    odd and even element do the add operation
    """
    res = []
    for item in group_list(lst, 2):
        if len(item) > 1:
            a, b = item
            res.append(a + b)
        else:
            a = item[0]
            res.append(a)
    return res


def double_iter(lst: list, mode='combinations'):
    """
    if the list is [A, B, C,D ]
    mode default value is combinations:
    which means no self-repeat and elements compare with no order.
    default mode will yield
    (A,B) (A,C) (A,D) (B,C) ...

    if set mode = product will yield
    which is equal two for-loop clause
    (A,A) (A,B) (A,C) (A,D) (B,A) (B,B) ...

    if set mode = permutations, will yield
    (A,B) (A,C) (A,D) (B,A) (B,C) (B,D) ...
    which means no self-repeat and elements compare with order.

    if set mode = combinations_with_replacement, will yield
    (A, A) (A, B) (A, C) (A, D) (B, B) (B, C) (B, D) ...
    which means with self-repeat and elements compare with no order.
    """

    if mode == 'combinations':
        return combinations(lst, 2)
    elif mode == 'product':
        return product(lst, repeat=2)
    elif mode == 'permutations':
        return permutations(lst, 2)
    elif mode == 'combinations_with_replacement':
        return combinations_with_replacement(lst, 2)


class NearlyPerfectList(UserList):
    """
    几乎完美列表

    将会要求指定完美匹配模板来检测异常区间

    在实践中推荐使用dataclass类并自定义 __eq__ 方法来封装数据
    """

    def find_anomaly_intervals(
            self,
            template: Optional[List],
            min_size: int = 8
    ):
        """
        递归划分区间，与完美模板逐位比较，找出异常区间。

        :param template:  完美模板列表（长度必须与 self.data 相同）
        :param min_size:  最小区间长度，小于此长度的区间不再细分
        """
        lst = self.data

        if len(template) != len(lst):
            raise ValueError("template 长度必须与 self.data 相同")

        anomalies = []  # 存储异常区间的 (start, end) 左闭右开

        def is_perfect_block(start: int, end: int) -> bool:
            """当前区间与模板对应切片完全相等即为正常"""
            return lst[start:end] == template[start:end]

        # 栈模拟递归，元素：(start, end)
        stack = [(0, len(lst))]

        while stack:
            start, end = stack.pop()

            # 取堆栈分析 完美的直接跳过
            if is_perfect_block(start, end):
                continue

            # 接下来是不完美区间分析
            length = end - start

            # 判断区间已经足够小 处理结束
            if length <= min_size:
                anomalies.append((start, end))
                continue
            else:
                # 不完美堆栈并且区间足够大
                # 对区间进行二分，分割任务进入队列
                size = length // 2
                block_end = start + size
                stack.append((start, block_end))

                rest_length = end - block_end
                if rest_length <= min_size:
                    # 剩余的部分很小了 直接判断一下结束本部分
                    if not is_perfect_block(block_end, end):
                        anomalies.append((block_end, end))
                        continue
                else:
                    # 后半段进去队列
                    stack.append((block_end, end))

        # 输出结果
        abnormal_data = []
        related_template_data = []

        anomalies.sort(key=lambda x: x[0])  # 确保有序
        print(f"共发现 {len(anomalies)} 个异常区间（最小区间长度 = {min_size}）：")
        for s, e in anomalies:
            if e - s == 1:
                print(f"  索引 [{s}]")
                abnormal_data.append([lst[s]])
                related_template_data.append([template[s]])
            else:
                print(f"  索引 [{s}, {e})")
                abnormal_data.append(lst[s:e])
                related_template_data.append(template[s:e])
        return abnormal_data, related_template_data


class NearlyOrderedList(NearlyPerfectList):
    """
    几乎有序列表，通过与完美排序模板逐位比较来检测异常区间。

    完美模块默认是由sorted自动生成，用户显式输入备用保留

    在实践中推荐使用dataclass类并自定义 __eq__  __lt__ 方法来封装数据
    """

    def find_anomaly_intervals(
            self,
            template: Optional[List] = None,
            min_size: int = 8,
    ):
        """
        递归划分区间，与完美排序模板逐位比较，找出异常区间。
        :param template:  完美排序模板列表，默认自动由sorted函数比对生成（长度必须与 self.data 相同）
        :param min_size:  最小区间长度，小于此长度的区间不再细分
        """
        if template is None:
            template = sorted(self.data)

        return super().find_anomaly_intervals(template, min_size)


def flatten(inlst):
    """
    make multiple layer list or tuple to one dimension list

        >>> flatten((1,2,(3,4),((5,6))))
        [1, 2, 3, 4, 5, 6]
        >>> flatten([[1,2,3],[[4,5],[6]]])
        [1, 2, 3, 4, 5, 6]

    """
    lst = []
    for x in inlst:
        if not isinstance(x, (list, tuple)):
            lst.append(x)
        else:
            lst += flatten(x)
    return lst
