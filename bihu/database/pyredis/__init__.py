#!/usr/bin/env python
# -*-coding:utf-8-*-



import redis
from dynaconf import settings


def get_redis_client(db=0):
    host = settings['redis'].get('host', 'localhost')
    port = settings['redis'].get('port', 6379)

    redis_client = redis.StrictRedis(host=host, port=port, db=db, decode_responses=True)
    return redis_client


redis_client = get_redis_client()

def set_redis(name, value, expiration=0):
    """
    expiration 过期时间=0 不过期

    """
    redis_client.set(name, value)

    if expiration:
        redis_client.expire(name, expiration)


def get_redis(name):
    return redis_client.get(name)