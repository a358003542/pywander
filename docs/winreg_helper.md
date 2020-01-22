## winreg_helper
windows的注册表读写工具
1. 默认的Key
```
    >>> HKEY_CURRENT_USER
    <regobj Key 'HKEY_CURRENT_USER'>
    >>> HKLM
    <regobj Key 'HKEY_LOCAL_MACHINE'>
```
2. 自组建Key 可以写上一连串path名字
```
    Key(parent, *name)
```
3. .subkeys() 列出所有该Key的子Key TODO 数据结构字典化支持按名字索引

4. .name 本Key的名字

5. .names 本Key完整路径名字

6. .get_subkey(name) 根据名字来向下获取子Key

7. .del_subkey(name) 删除某个子Key

8. .values() 列出该Key所包含的子值

9. .items() 列出该Key所包含的子值，不过返回的是字典格式

10. Key['name'] 实际获取某个Key的子值 没找到抛异常

11. Key['name'] = value 修改某个Key的子值

12. get(name) 试着获取某个Key的子值，没找到返回None

13. .delete() 删除本Key

14. .get_data(name) 试着获取某个Key的子值，直接返回值而不是Value对象



