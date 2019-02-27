#!/usr/bin/env python
# -*-coding:utf-8-*-


import logging

from urllib.parse import quote_plus

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

logger = logging.getLogger(__name__)


def build_mongodb_uri(host='localhost', username='', password=''):
    """
    mongodb://[username:password@]host1[:port1][,host2[:port2],...[,hostN[:portN]]][/[database][?options]]
    :return:
    """
    if username and password:
        uri = "mongodb://{username}:{password}@{host}".format(
            username=quote_plus(username),
            password=quote_plus(password),
            host=host
        )
    elif username and not password:
        uri = "mongodb://{username}@{host}".format(
            username=quote_plus(username),
            host=host
        )
    else:
        uri = "mongodb://{host}".format(
            host=host
        )
    return uri


def get_mongodb_client(host='localhost', port=27017, username='', password='', repset=None):
    dbport = int(port)

    mongodb_uri = build_mongodb_uri(host=host, username=username, password=password)
    try:
        if repset is None:
            mongodb_client = MongoClient(mongodb_uri,
                                         port=dbport)
        else:
            mongodb_client = MongoClient(mongodb_uri,
                                         replicaset=repset,
                                         port=dbport)
        return mongodb_client
    except ConnectionFailure as ex:
        logging.warning(ex)
