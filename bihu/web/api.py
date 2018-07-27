#!/usr/bin/env python
# -*- coding: utf-8 -*-


import logging

### memory对象最简单就是本模块的一个记录
### 或者redis数据库
memory = {}



class memorized_property(property):
    def __init__(self,*args,**kwargs):
        super(memorized_property,self).__init__(*args,**kwargs)

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        if self.fget is None:
            raise AttributeError("unreadable attribute")

        if obj.gen_memoryid is not None:
            self.name = obj.gen_memoryid() + '::' + self.fget.__name__
        else:
            self.name = '::' + self.fget.__name__

        if self.name in memory:
            logging.debug('from memory------------------------------')
            return memory[self.name]
        else:
            logging.debug('from computing##########################')
            value = memory[self.name] = self.fget(obj)
            return value

    def __set__(self, obj, value):
        if self.fset is None:
            raise AttributeError("can't set attribute")

        if obj.gen_memoryid is not None:
            self.name = obj.gen_memoryid() + '::' + self.fset.__name__
        else:
            self.name = '::' + self.fget.__name__

        memory[self.name] = value

    def __delete__(self, obj):
        if self.fdel is None:
            raise AttributeError("can't delete attribute")
        if obj.gen_memoryid is not None:
            self.name = obj.gen_memoryid() + '::' + self.fdel.__name__
        else:
            self.name = '::' + self.fget.__name__
        del memory[self.name]


class Api(object):
    def gen_memoryid(self):
        '''create a id string'''
        raise NotImplementedError