## number
### radix_conversion
数值转换。

给定一个数字，输入的数字可以是number型或者字符串型，然后指定要输出的数字的进制。默认输入的数字进制是十进制。

进制的输入支持 bin oct dec hex 和 2 8 10 16 。

输出的数字是字符串型。

```python

def radix_conversion(number, output_radix, input_radix=10):
    """
    number radix conversion.

    number: input can be a number or string
    output_radix:
    input_radix: the input number radix, default is 10

    the radix support list: ['bin', 'oct', 'dec', 'hex', 2, 8, 10, 16]

>>> radix_conversion(10, 'bin')
'1010'
>>> radix_conversion('0xff', 2, 16)
'11111111'
>>> radix_conversion(0o77, 'hex')
'3f'
>>> radix_conversion(100, 10)
'100'
>>> radix_conversion(100,1)
Traceback (most recent call last):
......
my_python_module.exceptions.OutOfChoiceError: radix is out of choice.

    """
```

### round_half_up
```python
def round_half_up(n, decimals=0):
    """
    实现常见的那种四舍五入，警告这只是一种近似，如果有精确的小数需求还是推荐使用decimal模块。
    """
```