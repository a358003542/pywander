#!/usr/bin/env python
# -*-coding:utf-8-*-


import os

import pandas as pd


class DataHandler(object):
    """
    read data source from
    - file
    - python  DataFrame dict ...
    - sql
    """

    def __init__(self, data=None, **kwargs):
        self.df = pd.DataFrame(data)

    def load_from_txt(self, filename, **kwargs):
        self.df = pd.read_csv(filename, **kwargs)

    def load_from_csv(self, filename, **kwargs):
        self.df = pd.read_csv(filename, **kwargs)

    def load_from_excel(self, filename, **kwargs):
        self.df = pd.read_excel(filename, **kwargs)

    def load_from_json(self, filename, **kwargs):
        self.df = pd.read_json(filename, **kwargs)

    def load_from_sql(self, sql_query, sql_conn, **kwargs):
        self.df = pd.read_sql(sql_query, sql_conn, **kwargs)

    def set_columns(self, columns):
        self.df.columns = columns

    def rename_column(self, origin_column_name, column_name):
        """
        默认的column 可用 0 1 2 来引用
        :param origin_column_name:
        :param column_name:
        :return:
        """
        d = {}
        d[origin_column_name] = column_name
        self.df.rename(columns=d, inplace=True)

    def rename_columns(self, columns):
        self.df.rename(columns=columns, inplace=True)
