## basic

### dict
some operation on python dict object.

#### compare_dict_include
```python
def compare_dict_include(d, include=None):
    """
    compare two dict object include or contained relationship

    return True : d totally contain the second dict

>>> compare_dict_include({'a':1},{})
True
>>> compare_dict_include({'a':1},{'a':2})
False
>>> compare_dict_include({'a':1},{'a':1})
True
>>> compare_dict_include({'a':1,'b':2},{'a':1})
True
>>> compare_dict_include({'a':1,'b':2},{'b':2})
True
    """
```

#### check_dict_has
```python
def check_dict_has(d, has=None):
    """
    does the dict object has some keys

>>> check_dict_has({'a':1,'b':2},[])
True
>>> check_dict_has({'a':1,'b':2},['a'])
True
>>> check_dict_has({'a':1,'b':2},['a','c'])
False
>>> check_dict_has({'a':1,'b':2},['a','b'])
True

    """
```


#### merge_dict
```text
def merge_dict(*args):
    """
    merge multi-dict, if there is a duplicate key, the value is decide by the last one.

    ref : http://stackoverflow.com/questions/38987/\
    how-can-i-merge-two-python-dictionaries-in-a-single-expression
    
merge_dict({'a': 1, 'b': 2}, {'b': 10, 'c': 11})
{'a': 1, 'b': 10, 'c': 11}

```

#### sorted_dict_by_value
```python
def sorted_dict_by_value(d, **kwargs):
    """
    sorted dict by it's value

>>> sorted_dict_by_value({'andy':5,'Andy':1,'black':9,'Black':55})
[('Andy', 1), ('andy', 5), ('black', 9), ('Black', 55)]

    """
```

### list
some operation on python list object.

#### del_list
```python

def del_list(lst, indexs):
    """
    del list base a index list

>>> del_list([0,1,2,3,4,5],[2,3])
[0, 1, 4, 5]
>>> lst = list(range(6))
>>> lst
[0, 1, 2, 3, 4, 5]
>>> del_list(lst,[2,3])
[0, 1, 4, 5]
>>> lst
[0, 1, 4, 5]
>>> del_list(lst,[0,2])
[1, 5]
>>> lst
[1, 5]

    """
```


#### group_list
```python
def group_list(lst, n=1):
    """
    group a list, in some case, it is maybe useful.

>>> list(group_list(list(range(10)),0))
Traceback (most recent call last):
AssertionError
>>> list(group_list(list(range(10)),1))
[[0], [1], [2], [3], [4], [5], [6], [7], [8], [9]]
>>> list(group_list(list(range(10)),2))
[[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]]
>>> list(group_list(list(range(10)),3))
[[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]
>>> list(group_list(list(range(10)),4))
[[0, 1, 2, 3], [4, 5, 6, 7], [8, 9]]

    """
```

### number
#### radix_conversion

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
