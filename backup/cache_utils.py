#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
import logging
import threading
from functools import wraps
from datetime import datetime
from dateutil.relativedelta import relativedelta

from diskcache import Cache

from pywander.unique_key import build_unique_key
from pywander.datetime import get_timestamp, get_dt_fromtimestamp

logger = logging.getLogger(__name__)


class CacheDB(object):
    """
    {
        "data": ...,
        "timestamp": ...
    }

    """
    _instance = None

    def __new__(cls, cache_path):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._cache = Cache(cache_path)
        return cls._instance

    @property
    def cache(self):
        return self._cache

    def set(self, key, value, **kwargs):
        """
        """
        self.cache.set(key, value, **kwargs)

    def get(self, key, **kwargs):
        return self.cache.get(key, **kwargs)


# 默认就是当前工作目录
cachedb = CacheDB('cachedb')


def default_use_cache_callback(cache_data, func, args, kwargs,
                               use_cache_oldest_dt=None):
    timestamp = cache_data.get('timestamp', get_timestamp())
    data_dt = get_dt_fromtimestamp(timestamp)

    if use_cache_oldest_dt is None:
        target_dt = datetime.now() - relativedelta(
            seconds=86400 * 14)  # default 14 days
    else:
        target_dt = use_cache_oldest_dt

    if data_dt < target_dt:  # too old then we will re-excute the function
        key = cache_data.get('key')
        data = func(*args, **kwargs)

        if data:
            cache_data['data'] = data
            cache_data['timestamp'] = str(get_timestamp())

            cachedb.set(key, cache_data)
            return data  # not important
        else:
            raise Exception(f'execute func {func.__name__} got no data return.')


def func_cache(use_key='', use_cache_oldest_dt=None,
               use_cache_callback=default_use_cache_callback):
    """
    this decorator will decorator a function and try to return a value based on
    cache.
    """

    def _mydecorator(func):
        @wraps(func)
        def wraper_func(*args, **kwargs):
            if not use_key:
                key = build_unique_key(func.__name__, *args, **kwargs)
            else:
                key = use_key

            cache_data = cachedb.get(key)

            if cache_data:
                logger.info('read data from cache ')
                use_cache_callback(cache_data, func, args, kwargs,
                                   use_cache_oldest_dt=use_cache_oldest_dt)
                return cache_data.get('data')
            else:
                logger.info(f'get data from excute func')
                data = func(*args, **kwargs)

                if data:
                    cache_data = {
                        'data': data,
                        'key': key,
                        "timestamp": str(get_timestamp())
                    }

                    cachedb.set(key, cache_data)
                    return data
                else:
                    raise Exception(
                        f'execute func {func.__name__} got no data return.')

        return wraper_func

    return _mydecorator

def _update_requests_web(cache_data, args):
    logger.info('update_requests_web')
    headers = {
        'user-agent': ua.random()
    }
    url = args[0]
    data = requests.get(url, headers=headers, timeout=30)

    cache_data['data'] = data
    cache_data['timestamp'] = str(get_timestamp())
    key = cache_data.get('key')

    cachedb.set(key, cache_data)
    return data

def use_cache_callback_requests_web(cache_data, func, args, kwargs,
                                    use_cache_oldest_dt=None):
    timestamp = cache_data.get('timestamp', get_timestamp())
    data_dt = get_dt_fromtimestamp(timestamp)

    if use_cache_oldest_dt is None:
        target_dt = datetime.now() - relativedelta(
            seconds=14)  # default 14 days
    else:
        target_dt = use_cache_oldest_dt

    if data_dt < target_dt:  # too old then we will re-excute the function
        t = threading.Thread(target=_update_requests_web,
                             args=(cache_data, args))
        t.daemon = True
        t.start()
@func_cache(use_cache_callback=use_cache_callback_requests_web)
def requests_web(url):
    """
    有数据则直接使用 没有数据则试着从网络上请求
    直接使用数据的时候会根据数据的时间戳来判断新旧，如果数据过旧则启动后台更新线程

    :param url:
    :return:
    """
    headers = {
        'user-agent': ua.random()
    }

    data = requests.get(url, headers=headers, timeout=30)

    return data