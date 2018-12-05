# bihu

个人学习研究python的结晶, 一个大杂烩性质的通用模块【但也不是什么都往里面扔，而是作者确实感觉到有实用价值】

MIT LICENSE.


## 安装
```
pip install bihu
```


## TODO

- 算法等各个问题继续丰富

- ml机器学习部分 在编写的时候，一方面要考虑轻耦合，各个接口各个层次都是开放的，可用的，另一方面考虑 pandas matplotlib keras等等工具更紧密的继承。

- plot_utils 绘图功能


## 功能简介
本模块文档只能这样简要介绍下【更详细的api介绍请查阅源码】，如果读者有使用需要可能更好的方案是复制copy到你那边的代码哪里去。


### gfun部分
初学python的可以看看里面的内容，定义了斐波那契函数和计算素数之类的。



### web部分
web部分是我研究爬虫的一些结晶，其中比较实用的有：

- 获得一个随机的User-Agent get_random_user_agent

- 将一个url，相对的或者绝对的，转成绝对url to_absolute_url

- 下载操作 download

### database部分
 database 里面放着很多便捷的对接数据库的通用操作模式。

- mongodb连接操作 get_mongodb_client

- mongodb插入操作 加入了去重逻辑 insert_item

- mongodb upsert 操作 upsert_item


- sqldb利用sqlalchemy完成连接操作，具体根据host，port等参数返回sqlalchemy支持的url create_sqlalchemy_url

- SQLDataBase类 输入sqlalchemy支持的url格式，连接数据库后的一些操作，本类主要用于sqlalchemy的非原生ORM操作。
```
        self._engine
        self._conn
        self._meta
        self._session
        self.execute  执行
        self.all_tables 所有table name
        self.get_table(table_name) 返回sqlalchemy的Table对象，内省，会更加健壮，也更加底层
```

- sqldb插入或者忽略操作 insert_or_ignore

- sqldb 插入或者更新操作 insert_or_update

- sqldb更新一个记录操作 update_one


### algorithms算法部分
个人学习算法的一些积累。


### ml机器学习部分
个人学习机器学习部分的一些积累，

- preprocessing 数据预处理支持
- reader 读取数据支持

- knn 很粗糙地对接了下knn算法 TODO

### utils部分
utils里面有很多便捷的函数支持。

#### admin_utils
提升管理员权限工具 admin_utils 用于在windows下提升脚本运行权限

- is_admin 判断是否是管理员权限
- run_as_admin 已管理员方式运行本脚本

```python
if __name__ == '__main__':
    if not is_admin():
        run_as_admin()
    else:
        main()
```

#### winreg_utils
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



- airflow_utils 对最小时间片的单个任务提供额外的运行状态记录支持

- 日期工具  date_utils

- 自然语言处理工具 nlp_utils

- 路径处理工具 path_utils

- 绘图支持工具 plot_utils 基于matplotlib的绘图便捷支持



