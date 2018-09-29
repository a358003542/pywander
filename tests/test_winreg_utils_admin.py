#!/usr/bin/env python
# -*-coding:utf-8-*-

import winreg


def test_winreg_utils():
    from bihu.utils.winreg_utils import Key, HKCR
    k = Key(HKCR, '.py', 'ShellNew', 'abc')
    k.delete()
