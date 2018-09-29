#!/usr/bin/env python
# -*-coding:utf-8-*-


def test_winreg_utils():
    from bihu.utils.winreg_utils import Key, HKCR
    k = Key(HKCR, '.py')

    print(k)


