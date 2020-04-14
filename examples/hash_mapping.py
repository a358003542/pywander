#!/usr/bin/env python
# -*-coding:utf-8-*-

import random
import string
import hashlib
from operator import add
from functools import reduce
from collections import defaultdict


def md5(key):
    return hashlib.md5(key.encode()).hexdigest()


def mapping(hashkey, n=10):
    return reduce(add, [ord(i) for i in hashkey]) % n


data = defaultdict(lambda: 0)


def random_string_generator():
    data = []
    random_length = random.randint(1, 100)
    for i in range(random_length):
        x = random.choice(string.ascii_lowercase + string.digits + ' ')
        data.append(x)
    return ''.join(data)


for i in range(100000):
    s = random_string_generator()

    c = mapping(md5(s))
    print(f'"{s}" mapping to bukket {c}')

    data[c] += 1

print(data)

