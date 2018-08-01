#!/usr/bin/env python
# -*-coding:utf-8-*-

from dynaconf import settings
from sqlalchemy.engine.url import URL


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
    if drivername.startswith('mysql') and 'charset' not in kwargs:
        kwargs['charset'] = 'utf8mb4'

    dburl = URL(drivername, username=username, password=password, host=host,
                port=port, database=database, query=kwargs)

    return dburl


sqldb_workflow_url = create_sqlalchemy_url('mysql+pymysql',
                                           host=settings['db_workflow'].get('host', 'localhost'),
                                           username=settings['db_workflow'].get('username'),
                                           password=settings['db_workflow'].get('password'),
                                           port=settings['db_workflow'].get('port', '3306'),
                                           database=settings['db_workflow'].get('dbname'))
