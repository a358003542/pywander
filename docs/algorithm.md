## algorithm
some algorithm implemented on python.


### binary_search
#### binary_search_func
```python

def binary_search_func(seq, target, func=lambda x: x, round_n=4, approx=True):
    """
    use binary search to solve f(x) = target problem, if the function is a
    monotonic function.

    seq  list or tuple
    target found target in which case is the f(x) = target
    func the monotonic function
    round_n accurate to how many decimal point
    approx the approx mode
    if approx=True found target or some nearly target, return it's index
    if approx=False  found target index otherwise return -1
    """
```

#### binary_search
```python
def binary_search(seq, target):
    """
    use the bisect_left.
    """
```
#### binary_insert
```python
def binary_insert(seq, target):
    """
    use the insort_left
    """
```

### quick_sort
#### quick_sort
```python
def quick_sort(seq):
    """
    10000 random number seq ：
    select_sort use time 3.0919713973999023
    quick sort use time 0.024930477142333984

    """
```

### select_sort
#### select_sort
```
def select_sort(seq):
```