#!/usr/bin/env python
# -*-coding:utf-8-*-

import pytest
from pywander.exceptions import NotIntegerError
from pywander.math.arithmetic import is_odd, prime, fibonacci, is_prime, is_even


def test_is_even():
    for i in [2, 4, -2, 0]:
        assert is_even(i)
    for i in [1, -1, 5]:
        assert not is_even(i)
    for i in [1.1, 0.0, 2.2, -2.2]:
        with pytest.raises(NotIntegerError):
            is_even(i)


def test_is_odd():
    for i in [2, 4, -2, 0]:
        assert not is_odd(i)
    for i in [1, -1, 5]:
        assert is_odd(i)
    for i in [1.1, 0.0, 2.2, -2.2]:
        with pytest.raises(NotIntegerError):
            is_odd(i)


def test_is_prime():
    for i in [2, 3, 5, 7, 199, 499]:
        assert is_prime(i) is True
    for i in [4, 6, 497]:
        assert is_prime(i) is False

    with pytest.raises(NotIntegerError):
        for i in [1.1, 0.0, 2.2, -2.2]:
            is_prime(i)


def test_prime():
    assert prime(4) == 7


def test_fibonacci():
    assert fibonacci(6) == 8
