#!/usr/bin/env python
# -*-coding:utf-8-*-

from bihu.database.mongodb.conn import mongodb

# 一般小站的缓存
collection_search = mongodb['search']
collection_book_info = mongodb['book_info']

# 存放着一些关于网络状态请求的额外的信息
collection_webs = mongodb['webs']



print('plugin mongodb_conn loaded.')