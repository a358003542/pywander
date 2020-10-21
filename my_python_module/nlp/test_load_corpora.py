#!/usr/bin/env python
# -*-coding:utf-8-*-


from nltk.text import Text
from my_python_module.nlp.corpus import gutenberg

laozi = Text(gutenberg.words("laozi_s.txt"))
lunyu = Text(gutenberg.words("lunyu_s.txt"))

from nltk import FreqDist
from my_python_module.nlp.chinese_stop_words import STOP_WORDS
from my_python_module.nlp.utils import is_empty_string

t = FreqDist(
    [i for i in laozi if (i not in STOP_WORDS and not is_empty_string(i))])
t.most_common(50)
