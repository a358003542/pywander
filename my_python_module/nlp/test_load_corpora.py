#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_python_module.nlp.corpus import laozi, lunyu, zh_gutenberg, xiyouji
from nltk import FreqDist
from my_python_module.nlp.chinese_stop_words import STOP_WORDS
from my_python_module.nlp.utils import is_empty_string

t = FreqDist(
    [i for i in laozi if (i not in STOP_WORDS and not is_empty_string(i))])
t.most_common(50)

