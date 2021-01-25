## dict
some operation on python dict object.

### compare_dict_include
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

### check_dict_has
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


### merge_dict
```text
def merge_dict(*args):
    """
    merge multi-dict, if there is a duplicate key, the value is decide by the last one.

    ref : http://stackoverflow.com/questions/38987/\
    how-can-i-merge-two-python-dictionaries-in-a-single-expression

merge_dict({'a': 1, 'b': 2}, {'b': 10, 'c': 11})
{'a': 1, 'b': 10, 'c': 11}

```

### sorted_dict_by_value
```python
def sorted_dict_by_value(d, **kwargs):
    """
    sorted dict by it's value

>>> sorted_dict_by_value({'andy':5,'Andy':1,'black':9,'Black':55})
[('Andy', 1), ('andy', 5), ('black', 9), ('Black', 55)]

    """
```