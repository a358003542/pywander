## number
### radix_conversion

```python
def radix_conversion(number, output_radix, input_radix=None):
    """
    number radix conversion.
    number+input_radix: if given number is a string, then you must give the input_radix parameter.
    the radix support input: ['bin', 'oct', 'dec', 'hex', 2, 8, 10, 16]

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