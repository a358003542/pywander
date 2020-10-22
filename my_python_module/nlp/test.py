#!/usr/bin/env python
# -*-coding:utf-8-*-

import nltk
text = nltk.word_tokenize("And now for something completely different")

nltk.pos_tag(text)


from my_python_module.nlp.utils import bigrams

list(bigrams(['more', 'is', 'said', 'than', 'done']))