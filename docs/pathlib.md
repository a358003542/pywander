## pathlib
### normalized_path
```
def normalized_path(path='.') -> str:
    """
    默认支持 ~ 符号

    返回的是字符串

    which default support the `~`
    """
```

### normalized_path_obj
```
def normalized_path_obj(path='.') -> Path:
    """
    默认支持 ~ 符号

    返回的是 Path 对象
    :param path:
    :return:
    """
```


### rm
```
def rm(path, recursive=False):
    """
    the function can remove file or empty directory(default).

    use `shutil.rmtree` to remove the non-empty directory,you need add `recursive=True`

    """
```

### mkdirs
```
def mkdirs(path, mode=0o777):
    """
    Recursive directory creation function base on os.makedirs
    with a little error handling.
    """
```

### ls
```
def ls(path=".", glob=False):
    """
    like ls common， return Path object

    if `glob` set to True, then you can use the glob language for ls.
    """
```

### ls_file
```
def ls_file(path=".", glob=False):
    """
    based on ls function but only return file.
    """
```

### ls_dir
```
def ls_dir(path=".", glob=False):
    """
    based on ls function, but only return directory.
    """
```

### pwd
```
def pwd():
    """
    get current directory
    """
```

### gen_filetree
```
def gen_filetree(startpath='.', filetype=""):
    """
    利用os.walk 遍历某个目录，收集其内的文件，返回
    (文件路径列表, 本路径下的文件列表)
    比如:
    (['shortly'], ['shortly.py'])
(['shortly', 'templates'], ['shortly.py'])
(['shortly', 'static'], ['shortly.py'])

    第一个可选参数 startpath  默认值 '.'
    第二个参数  filetype  正则表达式模板 默认值是"" 其作用是只选择某些文件
    如果是空值，则所有的文件都将被选中。比如 "html$|pdf$" 将只选中 html和pdf文件。
    """
```