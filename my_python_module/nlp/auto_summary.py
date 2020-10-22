#!/usr/bin/env python
# -*-coding:utf-8-*-


import logging
import heapq

from .chinese_stop_words import STOP_WORDS
from .utils import is_chinese
from .tokenize import ChineseSentenceTokenizer, JiebaTokenizer

logger = logging.getLogger(__name__)


def auto_summary(content, word_tokenizer=JiebaTokenizer(),
                 sent_tokenizer=ChineseSentenceTokenizer()):
    sentence_list = sent_tokenizer.tokenize(content)

    word_frequencies = {}
    for word in word_tokenizer.tokenize(content):
        if word not in STOP_WORDS and is_chinese(word):
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word] / maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in word_tokenizer.tokenize(sent):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores,
                                       key=sentence_scores.get)

    summary = ' '.join(summary_sentences)

    return summary
