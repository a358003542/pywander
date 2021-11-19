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

### auto_summary
将一篇文章按照句子或者段落分开，然后进行tf-idf评分。

word(tf) = Cword(target word count in sent)/C(all word count in sent)

word(idf) = log(C(sent count)/C(target word in sent count))

最后得出的摘要会按照原文顺序输出，只是选择性地将某些不重要的句子删除，你可以通过 max_len 来控制想要的摘要长度。


```
def auto_summary(content, word_tokenizer=None, sent_tokenizer=None,
                 stop_words=None, max_len=50):
```