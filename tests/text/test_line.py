import pytest

from pywander.text.line import is_blank_line

def test_is_blank_line():
    assert is_blank_line("\n")
    assert is_blank_line("   \n")
    assert not is_blank_line("Hello, World!\n")
    assert is_blank_line("\t\n")
    assert is_blank_line("")
    assert is_blank_line("   ")


