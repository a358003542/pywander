#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging
import importlib

PLUGIN_EXISTS = False
try:
    import bihu_plugins
    PLUGIN_EXISTS = True
except ImportError:
    pass

import importlib
import pkgutil

def iter_namespace(ns_pkg):
    """
    利用pkgutil.iter_modules遍历模块，
    输出如下：

    {'bihu_plugins.const':
        <module 'bihu_plugins.const' from 'd:\\mycode\\bihu\\bihu_plugins\\const.py'>,

        ns_pkg.__name__ 这里是 bihu_plugins, 然后加上个点，这样仍然可以正常引用。

    :param ns_pkg:
    :return:
    """
    return pkgutil.iter_modules(ns_pkg.__path__, ns_pkg.__name__ + ".")


def get_all_plugins():
    """
    返回插件信息
    :return:
    """
    plugins_data = {}

    if PLUGIN_EXISTS:
        plugins_data = {
            name: importlib.import_module(name)
            for finder, name, ispkg
            in iter_namespace(bihu_plugins)
        }

    return plugins_data


PLUGIN_MAPPING = {
    'const': 'bihu.const',
    'id_utils': 'bihu.utils.id_utils',
    'mongodb_conn': 'bihu.database.mongodb.conn',
    'sqldb_conn': 'bihu.database.sqldb.conn'
}

def get_plugin_module(plugin_data, current_module_name):
    for k, v in PLUGIN_MAPPING.items():
        if v == current_module_name:
            plugin_module = plugin_data['bihu_plugins.' + k]
            return plugin_module


def get_plugin_module_data(current_module_name):
    names = []
    plugin_data = get_all_plugins()
    plugin_module = get_plugin_module(plugin_data, current_module_name)

    if plugin_module:
        if "__all__" in plugin_module.__dict__:
            names = plugin_module.__dict__["__all__"]
        else:
            names = [x for x in plugin_module.__dict__ if not x.startswith("_")]

        return {k: getattr(plugin_module, k) for k in names}

