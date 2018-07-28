#!/usr/bin/env python
# -*-coding:utf-8-*-

from bihu.database.sqldb.conn import create_sqlalchemy_url
from dynaconf import settings


sqldb_search_url = create_sqlalchemy_url('mysql+pymysql',
                                         host=settings['db_search'].get('host', 'localhost'),
                                         username=settings['db_search'].get('username'),
                                         password=settings['db_search'].get('password'),
                                         port=settings['db_search'].get('port', '3306'),
                                         database=settings['db_search'].get('dbname'))


sqldb_workflow_url = create_sqlalchemy_url('mysql+pymysql',
                                         host=settings['db_workflow'].get('host', 'localhost'),
                                         username=settings['db_workflow'].get('username'),
                                         password=settings['db_workflow'].get('password'),
                                         port=settings['db_workflow'].get('port', '3306'),
                                         database=settings['db_workflow'].get('dbname'))

print('plugin sqldb_conn loaded.')