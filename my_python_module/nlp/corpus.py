#!/usr/bin/env python
# -*-coding:utf-8-*-

from nltk.corpus import PlaintextCorpusReader
from .tokenize import JiebaTokenizer, ChineseSentenceTokenizer


def load_corpus(root, word_tokenizer=JiebaTokenizer(),
                sent_tokenizer=ChineseSentenceTokenizer()):
    return PlaintextCorpusReader(root, r"(?!\.).*\.txt",
                                 word_tokenizer=word_tokenizer,
                                 sent_tokenizer=sent_tokenizer,
                                 encoding='utf8')


gutenberg = load_corpus('D:/nlp_data/corpora/gutenberg')
