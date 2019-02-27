#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging

from pymongo import errors

logger = logging.getLogger(__name__)


def insert_item(collection, item, unique_key=None):
    """
    mongodb的插入操作
    unique_key 确定插入的判断逻辑，由这些key的value来确定记录的唯一性

    :param collection:
    :param item:
    :param unique_key:
    :return:
    """
    if unique_key is None:
        try:
            collection.insert_one(item)
        except errors.DuplicateKeyError:
            logger.error('duplicate key error')
    else:
        key = {}
        if isinstance(unique_key, list):
            for k in unique_key:
                key[k] = item[k]
        else:
            key[unique_key] = item[unique_key]

        if collection.find_one(key):
            logger.info('record already exist: {item}'.format(item=item))
        else:
            collection.insert_one(item)


def upsert_item(collection, item, unique_key=None):
    """
    mongodb 的更新或者插入逻辑
    unique_key 来判断记录是否重复，

    :param collection:
    :param item:
    :param unique_key:
    :return:
    """
    if unique_key is None:
        try:
            collection.insert_one(item)
        except errors.DuplicateKeyError:
            logger.error('duplicate key error')
    else:
        key = {}
        if isinstance(unique_key, list):
            for k in unique_key:
                key[k] = item[k]
        else:
            key[unique_key] = item[unique_key]

        collection.update_one(key, {"$set": item}, upsert=True)


def get_timeslice_data(collection, field, start_dt, end_dt):
    """
    针对某个字段取一定时间段的记录
    :param collection:
    :param field:
    :param start_dt:
    :param end_dt:
    :return:
    """
    targets = collection.find(
        {field: {'$gte': start_dt, '$lte': end_dt}},
        no_cursor_timeout=True).batch_size(16)

    return targets
