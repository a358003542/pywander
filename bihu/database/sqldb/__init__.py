#!/usr/bin/env python
# -*-coding:utf-8-*-


import copy

from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table
from sqlalchemy.exc import OperationalError, NoSuchTableError
from sqlalchemy.engine import reflection
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

import logging

logger = logging.getLogger(__name__)


class SQLDataBase(object):
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
        self._orm = orm
        self._engine = create_engine(dburl)
        self._conn = self._engine.connect()
        self._meta = MetaData(bind=self._engine)
        self._session = Session(self._engine)

        if self._orm:
            self._AutoBase = automap_base(metadata=self._meta)

            if loadtables == 'ALL':
                self._meta.reflect()
            elif loadtables:
                self.reflect(loadtables)

            self._AutoBase.prepare()

    def all_tables(self):
        """
        当前sql数据库实际有的表格名列表。
        """
        if self._orm:
            return list(self._AutoBase.classes)
        else:
            self.insp = reflection.Inspector.from_engine(self._engine)
            return self.insp.get_table_names()

    def get_table(self, table_name):
        """
        获取sqlalchemy的Table对象
        :param table_name:
        :return:
        """
        if self._orm:
            self.reflect(table_name)
            return self._AutoBase.classes.get(table_name)
        else:
            try:
                return Table(table_name, self._meta, autoload=True)
            except NoSuchTableError:
                raise ValueError('No Such table name.')

    def reflect(self, only):
        """
        如果已经reflect了的将会pass掉
        """
        if isinstance(only, (list, tuple, set)):
            self._meta.reflect(only=only)
        elif isinstance(only, str):
            self._meta.reflect(only=[only])
        else:
            raise Exception("wrong type {}".format(type(only)))

    def create_table(self, table_name, columns):
        """
        创建 table, 如果 table 已存在, 则无任何动作
        :param table_name:
        :param columns:
        :return:
        """
        if table_name not in self._meta.tables:
            # deepcopy 的原因: 一个 Column object 引用的只能用于创建一个表, 这是 sqlalchemy 的机制
            table = Table(table_name, self._meta, *copy.deepcopy(columns))
            table.create(checkfirst=True)

    def insert_data(self, table_name, data):
        """
        往指定表插入数据

        当表不存在时, self.tables[table_name] 会报 KeyError 错误,
        其中 KeyError.message 为表名字, 可以捕捉这个错误来动态创建需要的表
        :param table_name:
        :param data: data 为数组形式的字典
        :return:
        """
        _table = self._meta.tables[table_name]
        self._conn.execute(_table.insert(), data)

    def execute(self, statement, *multiparams, **params):
        """
        执行 sql 语句
        :param statement:
        :return:
        """
        return self._conn.execute(statement, *multiparams, **params)

    def close(self):
        """
        关闭 proxy conn
        :return:
        """
        self._conn.close()

    @property
    def session(self):
        return self._session
