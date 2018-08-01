#!/usr/bin/env python
# -*-coding:utf-8-*-


from scrapy.loader.processors import *






## 加载插件
from bihu.utils.plugin_utils import get_plugin_module_data
plugin_module_data = get_plugin_module_data(__name__)
globals().update(plugin_module_data)
