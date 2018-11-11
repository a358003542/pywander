#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bihu.utils.nlp_utils import guess_chapter_id
from bihu.utils.nlp_utils import bigrams, trigrams, skipgrams


def test_guess_chapter_id():
    assert guess_chapter_id('第3103章') == 3103

    assert guess_chapter_id('第三十章') == 30
    assert guess_chapter_id('第三十一章') == 31

    assert guess_chapter_id('第一百零二章') == 102

    assert guess_chapter_id('第二百三十八章') == 238


def test_bigrams():
    assert list(bigrams([1, 2, 3, 4, 5])) == [(1, 2), (2, 3), (3, 4), (4, 5)]


def test_trigrams():
    assert list(trigrams([1, 2, 3, 4, 5])) == [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

def test_skipgrams():
    sent = "Insurgents killed in ongoing fighting".split()
    assert list(skipgrams(sent, 2, 2)) == [('Insurgents', 'killed'), ('Insurgents', 'in'), ('Insurgents', 'ongoing'), ('killed', 'in'), ('killed', 'ongoing'), ('killed', 'fighting'), ('in', 'ongoing'), ('in', 'fighting'), ('ongoing', 'fighting')]
    assert list(skipgrams(sent, 3, 2)) == [('Insurgents', 'killed', 'in'), ('Insurgents', 'killed', 'ongoing'), ('Insurgents', 'killed', 'fighting'), ('Insurgents', 'in', 'ongoing'), ('Insurgents', 'in', 'fighting'), ('Insurgents', 'ongoing', 'fighting'), ('killed', 'in', 'ongoing'), ('killed', 'in', 'fighting'), ('killed', 'ongoing', 'fighting'), ('in', 'ongoing', 'fighting')]
