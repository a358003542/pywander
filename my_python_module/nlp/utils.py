#!/usr/bin/env python
# -*-coding:utf-8-*-
import re


def is_empty_string(s):
    if re.match('[\s]+', s):
        return True
    else:
        return False
