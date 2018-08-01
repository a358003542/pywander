#!/usr/bin/env python
# -*-coding:utf-8-*-


"""
动态配置系统里面请类似下面做好定义：

[testing.mongodb]
host = '192.168.99.100'
port = 27017
username = ''
dbname = 'bihu'
password = ''

"""

from dynaconf import settings
from . import get_mongodb_client

mongodb_client = get_mongodb_client(host=settings['mongodb'].get('host'),
                                    username=settings['mongodb'].get('username', 'root'),
                                    password=settings['mongodb'].get('password', ''),
                                    port=settings['mongodb'].get('port', '27017'))

mongodb = mongodb_client[settings['mongodb'].get('dbname')]



