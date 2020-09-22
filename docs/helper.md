## helper
some third-party modules helper library.


### datetime_helper
need the `dateutil` module.


- is_same_year 输入两个datetime 对象，判断是否是同一年
- is_same_month  判断两个datetime对象是否是同一月
- is_same_day 判断两个datetime对象是否是同一天
- is_same_hour 判断两个datetime对象是否是同一时
- round_to_day     datetime对象round到天，其他归零
- round_to_hour datetime对象round到小时，更小的刻度归零
- round_to_minute  datetime对象round到分钟
- round_to_second datetime对象round到秒

- get_date_range 返回一个时间片列表，以当前时间为终点，向前数几个月
```
from utils.date_utils import get_date_range
get_date_range(5)
Out[3]: 
[datetime.datetime(2018, 10, 7, 2, 7, 1),
 datetime.datetime(2018, 11, 7, 2, 7, 1),
 datetime.datetime(2018, 12, 7, 2, 7, 1),
 datetime.datetime(2019, 1, 7, 2, 7, 1),
 datetime.datetime(2019, 2, 7, 2, 7, 1),
 datetime.datetime(2019, 3, 7, 2, 7, 1)]
```

- normal_format_now  标准格式 now '2018-12-21 15:39:20'

- normal_format_utcnow

- get_timestamp 获得当前的timestamp

- get_dt_fromtimestamp 根据timestamp获得对应的datetime对象

### matplotlib_helper
#### set_matplotlib_support_chinese
设置matplotlib支持中文

### pie_plot
绘制饼状图

### barh_plot
水平条形图

### hist_plot
绘制直方图

### scatter_plot
散点图 

输入的是 x,y 数据

### polyfit_plot
多项式拟合绘图

### pandas_helper
#### combine_df
```
def combine_df(df_value, old_df):
    """
    输入ndarray值，然后根据给的老df的column列名来输出一个新的df
    :param df_value:
    :param old_df:
    :return:
    """
```

#### change_df_type
```
def change_df_type(df, column_name, type):
    """
    输入 df column_name type
    将df的某个列的类型更改为某个type 比如float等

    :param df:
    :param column_name:
    :param type:
    :return:
    """
```

#### rename_df_columns
```
def rename_df_columns(df, columns):
    """
    重新设置列名
    """
```

#### rename_df_column_by_index
```
def rename_df_column_by_index(dataset, index, to):
    """
    将index column 名字修改为 to
    :param dataset:
    :param index:
    :param to:
    :return:
    """
```

#### rename_df_column_by_name
```
def rename_df_column_by_name(dataset, name, to):
    """
    将某个column 名字修改为 to
    :param dataset:
    :param name:
    :param to:
    :return:
    """
```

#### get_all_column
```
def get_all_column(df, column_name, remove_duplicate=True):
    """
    获取一列所有的值 默认去重
    :param column_name:
    :param remove_duplicate:
    :return:
    """
```

### sqlalchemy_helper
利用sqlalchemy完成连接操作

#### create_sqlalchemy_url 
创建sqlalchemy支持的url

```
def create_sqlalchemy_url(drivername, username=None, password=None, host=None,
                          port=None, database=None, **kwargs):
    """
    输出一个 sqlalchemy的 url，有一些额外的优化。

    :param drivername:
    :param username:
    :param password:
    :param host:
    :param port:
    :param database:
    :param kwargs:
    :return:
    """
```


#### SQLDataBase 
输入sqlalchemy支持的url格式，连接数据库后的一些操作，本类主要用于sqlalchemy的非原生ORM操作。

```
    def __init__(self, dburl, loadtables='ALL', orm=True, **kwargs):
        """
        创建连接 db 的连接对象, 数据库不存在时自动创建

        self._engine
        self._conn
        self._meta
        self._session
        self.execute  执行
        self.all_tables 所有table name
        self.get_table(table_name) 返回sqlalchemy的Table对象，内省，会更加健壮，也更加底层


        :param dburl: 连接数据库的 URL, 格式为:
                    dialect[+driver]://user:password@host/  # 注意需要以斜杠结尾
        :param kw:
        :return:
        """
```

#### insert_or_ignore
sqldb插入或者忽略操作
```
def insert_or_ignore(session, orm, item, unique_key, return_key=None):
    """
    sql常用操作  插入或者忽略

    unique_key 指定判断记录唯一性的字段

    return_key 指定返回记录的字段 默认None，对返回记录没有特别的要求，或者指定一个字段名来返回
    :param session:
    :param orm:
    :param item:
    :param unique_key:
    :param return_key:
    :return: True inserted False ignore
    """
```

#### insert_or_update
插入或者更新操作 
```
def insert_or_update(session, orm, item, unique_key,
                     update_check=lambda target, item: True):
    """
    sql 常用操作 插入或者更新逻辑

    update_check 默认把匹配到的记录作为第一个参数传过去，方便进行一些逻辑判断，然后决定是否更新记录

    返回 None,info
    或者 True, 'updated'
    :param session:
    :param orm:
    :param item:
    :param unique_key:
    :return: True 表示已经插入或者更新了 None 表示什么都没有 info updated 有更详细的信息
    """
```


#### update_one
sqldb更新一个记录操作
```
def update_one(session, orm, item, unique_key):
    """
    更新一条记录
    :param session:
    :param orm:
    :param unique_key:
    :return:
    """
```
