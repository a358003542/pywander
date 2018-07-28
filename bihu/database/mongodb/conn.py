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




## 加载插件
from bihu.utils.plugin_utils import get_plugin_module_data
plugin_module_data = get_plugin_module_data(__name__)
globals().update(plugin_module_data)
