## file
### bigfile_read
超大型文件读取，可以选择从哪一行开始读，然后读取多少行，然后直接退出。

```python
def bigfile_read(filename, process_line=None, line_start=0, line_count=10000,
                 mode='r', encoding='utf8'):
    """
    filename 要处理的文件名
    process_line 每一行的处理函数 默认打印动作 默认传入第一个参数 当前行数 第二个参数 具体行内容
    line_start 从哪一行开始处理 默认0
    line_count 总计要处理多少行
    mode 文件打开模式 默认 'r'
    encoding 文件打开编码 默认 'utf8'

    :return:
    """
```