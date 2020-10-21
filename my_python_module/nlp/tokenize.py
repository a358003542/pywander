#!/usr/bin/env python
# -*-coding:utf-8-*-

import jieba
from nltk import RegexpTokenizer
from my_python_module.basic.list import combine_odd_even

from nltk.tokenize.api import TokenizerI


class JiebaTokenizer(TokenizerI):
    def tokenize(self, s):
        return jieba.lcut(s)


class ChineseSentenceTokenizer(RegexpTokenizer):
    def __init__(self):
        RegexpTokenizer.__init__(self, r"(。|？|！)", gaps=True)

    def tokenize(self, text):
        res = super(ChineseSentenceTokenizer, self).tokenize(text)
        return combine_odd_even(res)
