## functools
### build_compose_function

```
def build_compose_function(*funcs):
    """
    组建一个符合函数流对象 数据处理流模式

    每个函数的参数是任意的 但严格意义上一个合格的数据流管道设计应该在进口数据格式和入口数据格式上做出一些规范

    现在做出如下规范 入口是字典格式 出口也是字典格式 当然内核更细小的粒度的函数不做如此要求，这个只是数据处理流那边
    :param args:
    :return:
    """
```
### build_stream_function
和 `build_compose_function` 函数比起来进一步规范流处理函数过程中传递的参数是一个字典值。

流处理操作模式
```text
filter_all = build_stream_function(filter_zh_ratio, filter_zhtext_length, filter_text_length)
```
这样就将多个过滤函数连接成为一个流处理函数。


### flatten
将 **多层** 列表或元组变成一维 **列表**
```text
>>> flatten((1,2,(3,4),((5,6))))
[1, 2, 3, 4, 5, 6]
>>> flatten([[1,2,3],[[4,5],[6]]])
[1, 2, 3, 4, 5, 6]
```

### sumall
将所有的数字都加起来，支持多层结构。
```python
def sumall(*args):
    """将所有的数字都加起来，支持多层结构。
>>> sumall(1,1,2,3,[1,2,3])
13
>>> sumall(1,1,2,3,[1,2,3],(4,5,6),[[5,5],[6]])
44
>>>
    """
```