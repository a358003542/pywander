## str

### random_string_generator
random string generator

随机字符串生成器，默认是可打印的字符，你可以输入一个字符串来指定想要的那些字符。

```python
import string
default_choice_string = string.printable

def random_string_generator(max_length=100,
                            choice_string=default_choice_string):
    """
    random string generator

    """
```