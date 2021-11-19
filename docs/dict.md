## dict
some operation on python dict object.

### compare_dict_include
检查字典的包含关系，如果返回True，则第二个字典完全被一个字典包含。

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
检查字典是否有某些key。
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
字典合并，后面的值会覆盖前面的key相同的值。
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
对字典按照值排序
```python
def sorted_dict_by_value(d, **kwargs):
    """
    sorted dict by it's value

>>> sorted_dict_by_value({'andy':5,'Andy':1,'black':9,'Black':55})
[('Andy', 1), ('andy', 5), ('black', 9), ('Black', 55)]

    """
```


def get_related_value(d, item):
    """
    找到字典中相关的值，不确定item在字典中是key还是value，
    则可以调用这个函数。
    如果item是key，则会返回该key对应的值
    如果item是value，则会试着从字典的值里面查找
    如果翻遍字典的key和value也找不到对应的item，则抛出
    ValueError异常
    """
    if item in d:
        return d[item]

    if item in d.values():
        return item

    raise ValueError("Can not found the related value.")


### get_related_value
```python
def get_related_value(d, item):
    """
    找到字典中相关的值，不确定item在字典中是key还是value，
    则可以调用这个函数。
    如果item是key，则会返回该key对应的值
    如果item是value，则会试着从字典的值里面查找
    如果翻遍字典的key和value也找不到对应的item，则抛出
    ValueError异常
    """
```