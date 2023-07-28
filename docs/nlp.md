## nlp
some nlp tools

### 中文停用词列表

```
from my_python_module.nlp.chinese_stop_words import STOP_WORDS
```

### nltk_utils
#### str2tuple
```python
def str2tuple(s, sep="/"):
    """
    """
```
#### bigrams
```python
def bigrams(sequence, **kwargs):
    """
    Return the bigrams generated from a sequence of items, as an iterator.
    For example:

        >>> list(bigrams([1,2,3,4,5]))
        [(1, 2), (2, 3), (3, 4), (4, 5)]
    """
```
#### FreqDist
统计词频
```python
from collections import defaultdict, Counter
class FreqDist(Counter):
    def __init__(self, samples=None):
        """
        """
```
### utils
#### is_contain_chinese
判断字符串是否含有中文
```python
def is_contain_chinese(check_str):
    """
    判断字符串中是否包含中文
    :param check_str: {str} 需要检测的字符串
    :return: {bool} 包含返回True， 不包含返回False
    """
```
