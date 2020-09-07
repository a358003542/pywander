## unique_key

### build_unique_key
```
def build_unique_key(base_key, *args, **kwargs):
    """
    缓存唯一id标识生成函数

    :param base_key: 基本的区分key值 比如函数名
    :param args: 必填参数
    :param kwargs: 其他参数
    :return:
    """
```

### random_md5
```
def random_md5(limit=None):
    """
    输出基于uuid1产生的md5标识
    limit 截取最前面的几个
    """
```