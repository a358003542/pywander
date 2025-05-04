#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pywander.text import guess_chapter_id, zh_number_to_int
from pywander.text.zh_number import zh_number


def test_zh_number():
    assert zh_number(0) == '零'
    assert zh_number(1) == '一'
    assert zh_number(11) == '一十一'
    assert zh_number(15156) == '一万五千一百五十六'
    assert zh_number(101) == '一百零一'
    assert zh_number(1001) == '一千零一'
    assert zh_number(10000001) == '一千万零一'


def test_zh_number_to_int():
    assert zh_number_to_int('一') == 1
    assert zh_number_to_int('十一') == 11
    assert zh_number_to_int('二十二') == 22
    assert zh_number_to_int('一百零三') == 103
    assert zh_number_to_int('三百四十五') == 345

    assert zh_number_to_int('1万6千') == 16000


def test_zh_number_all():
    assert zh_number_to_int(zh_number(15156)) == 15156


def test_guess_chapter_id():
    assert guess_chapter_id('第3103章') == 3103

    assert guess_chapter_id('第三十章') == 30
    assert guess_chapter_id('第三十一章') == 31

    assert guess_chapter_id('第一百零二章') == 102

    assert guess_chapter_id('第二百三十八章') == 238

