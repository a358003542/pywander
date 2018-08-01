#!/usr/bin/env python
# -*-coding:utf-8-*-




class TakeFirstShiftLeftThree(object):
    """
    scrapy 就是这种形式，有个好处就是利用初始化过程可以带一些参数
    """
    def __call__(self, values):
        for value in values:
            if value is not None and value != '':
                return value[3:]