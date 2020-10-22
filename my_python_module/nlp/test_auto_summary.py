#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_python_module.nlp.corpus import zh_gutenberg
from my_python_module.nlp.auto_summary import auto_summary

summary = auto_summary(zh_gutenberg.raw('xiyouji_s.txt'))

