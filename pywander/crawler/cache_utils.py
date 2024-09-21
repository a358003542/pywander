#!/usr/bin/env python
# -*-coding:utf-8-*-

import os
import logging
from functools import wraps
from datetime import datetime
from dateutil.relativedelta import relativedelta

from diskcache import Cache

from pywander.unique_key import build_unique_key
from pywander.datetime import get_timestamp, get_dt_fromtimestamp
from pywander.config import load_config


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



APP_NAME = load_config().get('APP_NAME', 'pywander')

if APP_NAME == 'pywander':
    logger.warning("你还没有加载好自己的应用配置文件")

user_data_path = os.path.expanduser(
    os.path.join('~', 'AppData', 'Roaming', APP_NAME))

if not os.path.exists(user_data_path):
    os.mkdir(user_data_path)

cache_path = os.path.join(user_data_path, 'cache')
cachedb = CacheDB(cache_path)


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
            raise Exception(
                f'execute func {func.__name__} got no data return.')


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

