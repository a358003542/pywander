#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from my_python_module.common import str2pyobj
from my_python_module.basic.dict import merge_dict
from my_python_module.basic.list import del_list
from my_python_module.basic.number import radix_conversion
from my_python_module.exceptions import OutOfChoiceError


def test_number_radix_conversion():
    assert radix_conversion(10, 'bin') == '1010'
    assert radix_conversion('0xff', 2, 16) == '11111111'
    assert radix_conversion(0o77, 'hex') == '3f'
    assert radix_conversion(100, 10) == '100'
    with pytest.raises(OutOfChoiceError):
        radix_conversion(100, 1)


def test_del_list():
    assert del_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                    [2, 5, 9]) == [0, 1, 3, 4, 6, 7, 8]


def test_str2pyobj():
    test_list = {}
    # test int
    test_list['int'] = '72'
    # test float
    test_list['float'] = '3.14'
    # test 'abc.html'
    test_list['str'] = 'abc.html'
    # test list
    test_list['list'] = '[1,2,3]'
    # test True
    test_list['bool'] = 'True'

    for t, inval in test_list.items():
        outval = str2pyobj(inval)
        assert str(type(outval)).split("\'")[1] == t


def test_merge_dict():
    x = {'a': 1, 'b': 2}
    y = {'b': 10, 'c': 11}
    res = merge_dict(x, y)
    assert res == {'a': 1, 'c': 11, 'b': 10}
