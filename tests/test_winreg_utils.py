#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest

@pytest.mark.skip(reason="i have test it")
def test_winreg_utils():
    from mymodule.utils.winreg_utils import Key, HKCR
    k = Key(HKCR, '.py')

    print(k)


