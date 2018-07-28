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






## 加载插件
from bihu.utils.plugin_utils import get_plugin_module_data
plugin_module_data = get_plugin_module_data(__name__)
globals().update(plugin_module_data)