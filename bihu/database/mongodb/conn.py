#!/usr/bin/env python
# -*-coding:utf-8-*-


"""

这里放着实际的一些连接配置

"""

from dynaconf import settings
from . import get_mongodb_client

mongodb_client = get_mongodb_client(host=settings['mongodb'].get('host'),
                                    username=settings['mongodb'].get('username', 'root'),
                                    password=settings['mongodb'].get('password', ''),
                                    port=settings['mongodb'].get('port', '27017'))

mongodb = mongodb_client[settings['mongodb'].get('dbname')]



##################################################################
#
# 一些实际的便捷配置
#
###################################################################

# 一般小站的缓存
collection_search = mongodb['search']
collection_book_info = mongodb['book_info']

# 存放着一些关于网络状态请求的额外的信息
collection_webs = mongodb['webs']
