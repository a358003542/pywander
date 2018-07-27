#!/usr/bin/env python
# -*-coding:utf-8-*-

import logging
logger = logging.getLogger(__name__)

from bihu.utils.log_utils import FluentdLogger

fluentd_logger = FluentdLogger()


def insert_or_ignore(session, orm, item, unique_key, return_key=None):
    """
    sql常用操作  插入或者忽略

    unique_key 指定判断记录唯一性的字段

    return_key 指定返回记录的字段 默认None，对返回记录没有特别的要求，或者指定一个字段名来返回
    :param session:
    :param orm:
    :param item:
    :param unique_key:
    :param return_key:
    :return: True inserted False ignore
    """
    key = {}
    if isinstance(unique_key, list):
        for k in unique_key:
            key[k] = item[k]
    else:
        key[unique_key] = item[unique_key]

    q = session.query(orm).filter_by(**key).first()

    if not q: # insert or ignore
        session.add(orm(**item))
        session.commit()

        #fluentd_logger.send('sqldb_{0}'.format(orm.__tablename__), {'op_name': 'insert', 'op_data': item })

        if not return_key:
            logger.debug('insert a record to sql database.')
            return True, None
        else:
            first = session.query(orm).filter_by(**key).first()

            return_key = getattr(first, return_key)
            logger.debug('insert {0} to sql database.'.format(return_key))
            return True, return_key
    else:
        if not return_key:
            logger.debug('record already exist in sql database.')
            return False, None # True表示记录已存在，有的时候有用
        else:
            return_key = getattr(q, return_key)
            logger.debug('record {0} already exist in sql database.'.format(return_key))
            return False, return_key



def insert_or_update(session, orm, item, unique_key, update_check=lambda target,item: True):
    """
    sql 常用操作 插入或者更新逻辑

    update_check 默认把匹配到的记录作为第一个参数传过去，方便进行一些逻辑判断，然后决定是否更新记录

    返回 None,info
    或者 True, 'updated'
    :param session:
    :param orm:
    :param item:
    :param unique_key:
    :return: True 表示已经插入或者更新了 None 表示什么都没有 info updated 有更详细的信息
    """
    key = {}
    if isinstance(unique_key, list):
        for k in unique_key:
            key[k] = item[k]
    else:
        key[unique_key] = item[unique_key]

    q = session.query(orm).filter_by(**key).first()

    if not q:
        session.add(orm(**item))
        session.commit()

        #fluentd_logger.send('sqldb_{0}'.format(orm.__tablename__), {'op_name': 'insert', 'op_data': item})
        logger.debug('insert a record to sql database.')
        return True,'inserted'
    else:
        if update_check(q,item):
            for k,v in item.items():
                setattr(q, k, v)
            session.commit()

            #fluentd_logger.send('sqldb_{0}'.format(orm.__tablename__), {'op_name': 'update', 'op_data': item})
            logger.debug('updated a record in sql database.')
            return True, 'updated'
        else:
            logger.debug('update_check is not satisfied.')
            return None, 'passed'

        

def update_one(session, orm, item, unique_key):
    """
    更新一条记录
    :param session:
    :param orm:
    :param unique_key:
    :return:
    """
    key = {}
    if isinstance(unique_key, list):
        for k in unique_key:
            key[k] = item[k]
    else:
        key[unique_key] = item[unique_key]

    q = session.query(orm).filter_by(**key).first()

    if not q:
        return None
    else:
        for k, v in item.items():
            setattr(q, k, v)
        session.commit()

        logger.debug('updated a record in sql database.')
        return True


