## winreg
windows的注册表读写工具

### 默认的Key
```
    >>> HKEY_CURRENT_USER
    <regobj Key 'HKEY_CURRENT_USER'>
    >>> HKLM
    <regobj Key 'HKEY_LOCAL_MACHINE'>
```
### Key
自组建Key 可以写上一连串path名字
```
    Key(HKLM, '\where\where')
    Key(HKLM, ['where','where'])
    Key(parent, names)

Key(HKLM, ['SOFTWARE', 'Microsoft', 'Windows', 'CurrentVersion', 'Uninstall'])
<regobj Key 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall'>
```

默认 `create=True` ，也就是会自动创建Key，如果设置为 `False` 而Key不存在会抛出 OSError

### subkeys
列出本Key的所有子Key

```text
key.subkeys()
```

### name
本Key的名字
```text
key.name
```
### names
本Key完整路径名字
```text
Key.names
```

### get_subkey
根据名字来向下获取子Key 
```text
key.get_subkey(name)
```

### del_subkey
删除某个子Key
```text
key.del_subkey(name)
```

### values
列出该Key所包含的子值
```text
key.values()
```

### items
列出该Key所包含的子值，不过返回的是字典格式
```text
key.items()
```
### Key的子值操作
```text
Key['name'] 实际获取某个Key的子值 没找到抛异常
Key['name'] = value 修改某个Key的子值
key.get(name) 试着获取某个Key的子值，没找到返回None
Key[''] = 'what' 默认的子值
key.get_data(name) 试着获取某个Key的子值，直接返回值而不是Value对象
```

### delete
删除本Key
```
key.delete() 
```





