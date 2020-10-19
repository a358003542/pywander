#!/usr/bin/env python
# -*-coding:utf-8-*-


import os
from bs4 import BeautifulSoup

import logging

logger = logging.getLogger(__name__)


def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
    for ch in check_str:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False


def is_chinese(string):
    """
    检查整个字符串是否为中文
    Args:
        string (str): 需要检查的字符串,包含空格也是False
    Return
        bool
    """
    for chart in string:
        if chart < u'\u4e00' or chart > u'\u9fff':
            return False
    return True


from .chinese_stop_words import STOP_WORDS


def auto_summary(content):
    soup = BeautifulSoup(content, 'html.parser')
    page_text = soup.get_text()
    page_text = ' '.join(page_text.split())

    dict_path = os.path.join(os.path.dirname(__file__), 'blog_dict.txt')
    import nltk
    import jieba

    jieba.load_userdict(dict_path)

    article_text = page_text.replace('。', '.')

    sentence_list = nltk.sent_tokenize(article_text)

    word_frequencies = {}
    for word in jieba.lcut(article_text):
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
        for word in jieba.lcut(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    import heapq
    summary_sentences = heapq.nlargest(7, sentence_scores,
                                       key=sentence_scores.get)

    summary = ' '.join(summary_sentences)

    return summary
