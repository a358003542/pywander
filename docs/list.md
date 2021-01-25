## list
some operation on python list object.

### del_list
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


### group_list
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

### double_iter
```
def double_iter(lst: list, mode='combinations'):
    """
    if the list is [A, B, C,D ]
    mode default value is combinations:
    which means no self-repeat and elements compare with no order.
    default mode will yield
    (A,B) (A,C) (A,D) (B,C) ...

    if set mode = product will yield
    which is equal two for-loop clause
    (A,A) (A,B) (A,C) (A,D) (B,A) (B,B) ...

    if set mode = permutations, will yield
    (A,B) (A,C) (A,D) (B,A) (B,C) (B,D) ...
    which means no self-repeat and elements compare with order.

    if set mode = combinations_with_replacement, will yield
    (A, A) (A, B) (A, C) (A, D) (B, B) (B, C) (B, D) ...
    which means with self-repeat and elements compare with no order.
    """
```