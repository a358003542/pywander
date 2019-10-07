## sqlalchemy_helper
利用sqlalchemy完成连接操作

- create_sqlalchemy_url 创建sqlalchemy支持的url

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