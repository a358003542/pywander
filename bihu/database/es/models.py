#!/usr/bin/env python
# -*-coding:utf-8-*-


"""
elasticsearch database work collections
"""

# from datetime import datetime
#
# from elasticsearch import Elasticsearch
#
# from elasticsearch_dsl import DocType, Date, Integer, Keyword, Text
#
#
# class AllBooks(DocType):
#     """
#     o = ObjectId()
#     o == ObjectId(str(o))
#
#     "unique_id" 所有书籍的唯一id 包括source的不同
#     "first_chapters_is_fee" : Long
#     "chapter_title" : Keyword
#     "chapters_num" : Long
#     "is_remove" : Long
#     "book_name" : ik_max_word Text
#     "first_chapters_link" : Text
#     "book_desc" :
#     "title" :
#
#     """
#     unique_id = Keyword()
#     author = Keyword() # 作者名 精确搜索
#     name = Keyword() # 书名 精确搜索
#     chapter_id = Integer()
#     title = Text(analyzer='ik_max_word', fields={'raw': Keyword()}) # title 支持模糊搜索和精确搜索
#
#     book_type = Keyword()
#     content = Text(analyzer='ik_smart')
#
#     created_at = Date()
#
#     class Meta:
#         index = 'all_books'
#
#     def save(self, **kwargs):
#         """
#         自动填充doc创建时间
#         自动填充_id 根据unique_id
#         """
#         self.created_at = datetime.utcnow()
#         self.meta.id = self.unique_id
#
#         super().save(**kwargs)