#!/usr/bin/env python
# -*-coding:utf-8-*-

from dynaconf import settings
from datetime import datetime

from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# from .conn import sqldb_search_url
#
# engine = create_engine(sqldb_search_url)
# metadata = MetaData(bind=engine)
# Base = declarative_base(bind=engine)
# Session = sessionmaker(bind=engine)
# session = Session()

#
# class AllBooks(Base):
#     """
#     爬取书籍基本入口信息
#     """
#     __tablename__ = 'bh_all_books'
#
#     id = Column(Integer, primary_key=True)
#
#     author_name = Column(String(255), nullable=False, index=True)
#     book_name = Column(String(511), nullable=False, index=True)
#
#     source = Column(String(255))
#     source_book_id = Column(String(511))
#     book_url = Column(String(511))
#
#     failed_count = Column(Integer, default=0)
#
#     created_time = Column(DateTime, default=datetime.utcnow)
#     updated_time = Column(DateTime, onupdate=datetime.utcnow)
#     status = Column(Integer, default=0)  # 0 初始化 1 已更新
#
#     # source source_book_id 唯一性约束
#     __table_args__ = (UniqueConstraint('source', 'source_book_id', name='_unqiue_source_book_id'),
#                       )
#
#
# class AllBookInfo(Base):
#     """
#     创建书籍必要信息
#     """
#     __tablename__ = 'bh_all_book_info'
#
#     id = Column(Integer, primary_key=True)
#
#     source = Column(String(255))
#     source_book_id = Column(String(511))
#
#     book_url = Column(String(511))
#     book_name = Column(String(511), nullable=False, index=True)
#     author_name = Column(String(255), nullable=False, index=True)
#     tag = Column(String(511))
#     intro = Column(Text)
#     cover = Column(String(511))
#
#     book_status = Column(String(255))  # 连载中 完本
#
#     gender = Column(String(127))
#     category = Column(String(127))
#     sub_category = Column(String(127))
#
#     word_count = Column(Integer)
#
#     latest_chapter_url = Column(String(511))
#     latest_chapter_updated_time = Column(DateTime)
#     latest_chapter_title = Column(String(511))
#
#     book_shelf_time = Column(DateTime)
#
#     created_time = Column(DateTime, default=datetime.utcnow)
#     updated_time = Column(DateTime, onupdate=datetime.utcnow)
#     status = Column(Integer, default=0)  # 0 初始化 1 已更新
#     novel_id = Column(Integer)
#
#     failed_count = Column(Integer, default=0)
#
#     # source source_book_id 唯一性约束
#     __table_args__ = (UniqueConstraint('source', 'source_book_id', name='_unqiue_source_book_id'),
#                       )

#
# class NovelChapter(object):
#     _mapper = {}
#
#     @staticmethod
#     def model(book_id):
#         table_index = book_id % 100
#         class_name = 'NovelChapter_{0}'.format(table_index)
#
#         ModelClass = NovelChapter._mapper.get(class_name, None)
#         if ModelClass is None:
#             ModelClass = type(class_name, (Base,), {
#                 '__module__': __name__,
#                 '__name__': class_name,
#                 '__tablename__': 'bh_novel_chapter_{0}'.format(table_index),
#
#                 'id': Column(Integer, primary_key=True),
#                 'book_id': Column(Integer, nullable=False),
#                 'source': Column(String(255)),
#                 'source_book_id': Column(String(511)),
#                 'chapter_unique_id': Column(String(511), index=True),
#
#                 'volumn_title': Column(String(511)),
#                 'volumn_type': Column(String(63)),
#                 'volumn_count': Column(Integer, default=0),
#
#                 'chapter_title': Column(String(511)),
#                 'chapter_url': Column(String(511)),
#                 'chapter_count': Column(Integer),
#                 'chapter_type': Column(String(63)),
#                 'word_num': Column(Integer),
#                 'chapter_updated_time': Column(DateTime),
#
#                 'created_time': Column(DateTime, default=datetime.utcnow),
#                 'updated_time': Column(DateTime, onupdate=datetime.utcnow),
#                 'status': Column(Integer, default=0),  # 0 初始化 1 已更新
#                 'novel_id': Column(Integer),
#             })
#             NovelChapter._mapper[class_name] = ModelClass
#
#         return ModelClass
#
#
# for i in range(100):
#     NovelChapter.model(i)

#
# class PageParseRule(Base):
#     """
#     定义页面分析的爬取规则
#
#     op 是很核心的一个字段，定义格式如下 扁平结构就是好：
#     python 就是一行一行的，这里也一行一行的刷，有如下行类型：
#     footer_loader = loader.nested_xpath('//footer')  add_nested_loader
#     footer_loader.add_xpath('social', 'a[@class = "social"]/@href') nested_loader_add_xpath
#     l.add_xpath('name', '//div[@class="product_name"]') loader_add_xpath
#     l.add_css('stock', 'p#stock]') loader_add_css
#     l.add_value('last_updated', 'today')  loader_add_value
#
#
#     [
#         {
#         op_type  loader_add_xpath add_nested_loader loader_add_css loader_add_value nested_loader_add_xpath
#         field_name
#         nested_loader_name
#         op_string 具体操作字符串
#         processor # 定义在 bihu.rt.processor 里面的各个后处理器
#         },
#     ]
#
#     """
#     __tablename__ = 'bh_page_parse_rule'
#
#     id = Column(Integer, primary_key=True)
#
#     name = Column(String(255), nullable=False, index=True, unique=True)  # 爬虫名字
#     url_regex = Column(String(1023), nullable=False)  # 爬虫分发
#
#     op = Column(JSON, nullable=False)
#
#     description = Column(String(511))
#     created_time = Column(DateTime, default=datetime.utcnow)
#     updated_time = Column(DateTime, onupdate=datetime.utcnow)
