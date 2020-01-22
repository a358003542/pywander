## functools_helper

### build_stream_function
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