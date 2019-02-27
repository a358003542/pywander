#!/usr/bin/env python
# -*-coding:utf-8-*-


"""

show how to talk to windows dll

"""

import ctypes
import os

"""
依赖dll必须修改系统变量PATH才能工作，调试模式打开，正式的根据exe所在路径即可正常工作
"""

abs_path_current = os.path.abspath('.')  # 当前工作目录
os.environ['PATH'] = abs_path_current + os.pathsep + os.environ['PATH']


def get_libdll(dll_path):
    """

    :param dll_path:
    :return:
    """

    libdll = ctypes.windll.LoadLibrary()
