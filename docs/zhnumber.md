## zhnumber

### zhnumber
```
def zhnumber(number):
    """
    输入一个整数值返回中文表达的字符串

    :param int:
    :return:
    """
```

输入一个数字转成一百零一这样的表达：

```text
assert zhnumber(0) == '零'
assert zhnumber(1) == '一'
assert zhnumber(15156) == '一万五千一百五十六'
assert zhnumber(101) == '一百零一'
assert zhnumber(1001) == '一千零一'
assert zhnumber(10000001) == '一千万零一'
```


### int_zhnumber
```
def int_zhnumber(string):
    """
    将 一百一 或者 一百零一 这样的表达 转换称为 数字

    字符串组成只允许是:
    零一二三四五六七八九十百千万壹贰叁肆伍陆柒捌玖拾佰仟萬 此外还有 ‘0123456789’

    推荐的输入是标准中文数字格式，不过1万5千这样的不是很规范的格式也是支持的

    >>> int_zhnumber('一百')
    100
    >>> int_zhnumber('二十二')
    22
    >>> int_zhnumber('1万6千')
    16000

    ref https://github.com/binux/binux-tools/blob/master/python/chinese_digit.py
    """
```

将 一百一 或者 一百零一 这样的表达 转换称为 数字

```text
assert int_zhnumber('十一') == 11
assert int_zhnumber('二十二') == 22
assert int_zhnumber('一百零三') == 103
assert int_zhnumber('三百四十五') == 345

assert int_zhnumber('1万6千') == 16000
```