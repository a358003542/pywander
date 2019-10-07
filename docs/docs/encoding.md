## encoding

### convert_encoding
将某个字符串从某个编码转成某个编码
```text
convert_encoding(origin_string, origin_encoding, to_encoding,
                     errors='ignore')
```


### print_encoding_convert_tab
打印字符串编码转换列表，用于侦测某个字符串发生乱码之后原来的编码是多少。

安装 `tabulate` 模块之后显示效果更佳。