#!/usr/bin/env python
# -*-coding:utf-8-*-


from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from database.sqldb import SQLDataBase


sqldb_lianzai = SQLDataBase('your_sqlalchemy_conn', loadtables='xc_novels')



engine = create_engine('your_sqlalchemy_conn')
Session = sessionmaker(bind=engine)
session = Session()

XCNovels = sqldb_lianzai.get_table('xc_novels') # the sqlalchemy orm class
