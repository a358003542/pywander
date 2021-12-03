## cache_utils
need `diskcache` module.

### CacheDB
a simple wrapper for the diskcache `Cache` object, make it singleton and support the `set` and `get` method, which is like use a dict.

一个diskcache `Cache` 对象的简单封装，让其单例并支持`get` 和 `set` 方法，这就像在使用一个字典对象。

简单的使用就是如下：
```python
from my_python_module.cache_utils import cachedb

cachedb.set('a', 1)
cachedb.get('a')
```
缓存地点就是当前脚本工作地下的 `cachedb` 文件夹。

### func_cache
this decorator will decorator a function and try to return a value based on cache.

这是一个函数装饰器，装饰一个函数将会自动缓存该函数的执行结果，下次将直接调用结果而不是执行函数。