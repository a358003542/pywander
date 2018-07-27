#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
this file provide a python2-3 compatible solution
it has members:

本文引入了python2和python3兼容的统一的类型名字，只适合用在isinstance判断中，不推荐用于强制类型转换，if so it is too overhead。


* ispy2  ispy3  is_py2  is_py3 is_py30 ispy30 .....
* is_windows is_linux
* json module
* urlparse urlunparse
* urljoin urlsplit urldefrag urlencode
* quote unquote quote_plus unquote_plus
* python2 cookielib python3 just import cookielib
* StringIO
* OrderedDict
* str bytes
* reduce


"""

import sys
version_major = sys.version_info.major
version_minor = sys.version_info.minor
######
is_py3 = ispy3 = version_major == 3
is_py2 = ispy2 = version_major == 2
######
is_py30 = ispy30 = (is_py3 and version_minor == 0)
is_py31 = ispy31 = (is_py3 and version_minor == 1)
is_py32 = ispy32 = (is_py3 and version_minor == 2)
is_py33 = ispy33 = (is_py3 and version_minor == 3)
is_py34 = ispy34 = (is_py3 and version_minor == 4)
is_py35 = ispy35 = (is_py3 and version_minor == 5)
is_py36 = ispy36 = (is_py3 and version_minor == 6)
#######
is_py24 = ispy24 = (is_py2 and version_minor == 4)
is_py25 = ispy25 = (is_py2 and version_minor == 5)
is_py26 = ispy26 = (is_py2 and version_minor == 6)
is_py27 = ispy27 = (is_py2 and version_minor == 7)


# ---------
# Platforms
# ---------
is_windows = 'win32' == sys.platform.lower()
is_linux = 'linux' == sys.platform.lower()
is_msys = 'msys' == sys.platform.lower()


#######################################################
# learning from requests.compat.py
######################################################
try:
    import simplejson as json
except (ImportError, SyntaxError):
    # simplejson does not support Python 3.2, it throws a SyntaxError
    # because of u'...' Unicode literals.
    import json

if ispy2:
    from urllib import quote, unquote, quote_plus, unquote_plus, urlencode
    from urlparse import urlparse, urlunparse, urljoin, urlsplit, urldefrag
    import cookielib
    from StringIO import StringIO
    from .py2backport.ordered_dict import OrderedDict

    builtin_str = str
    bytes = str
    str = unicode
    basestring = basestring
    numeric_types = (int, long, float)

    reduce = reduce

elif ispy3:
    from urllib.parse import urlparse, urlunparse, urljoin, urlsplit, urlencode, quote, unquote, quote_plus, unquote_plus, urldefrag
    from io import StringIO
    from collections import OrderedDict

    builtin_str = str
    str = str
    bytes = bytes
    basestring = (str, bytes)
    numeric_types = (int, float)

    from functools import reduce




# if __name__ == '__main__':
