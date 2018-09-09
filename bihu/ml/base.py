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
    def __init__(self, data_source=None, data_source_type='file', read_data_kwargs=None):
        self.data_source = data_source
        self.read_data_kwargs = read_data_kwargs if read_data_kwargs is not None else {}

        self.df = None

        if data_source_type == 'file':
            _, ext = os.path.splitext(self.data_source)
            ext = ext.lower()[1:]

            if ext in ['csv', 'txt']:
                self.df = pd.read_csv(self.data_source, **self.read_data_kwargs)
            elif ext in ['xlsx']:
                self.df = pd.read_excel(self.data_source, **self.read_data_kwargs)
        elif data_source_type == 'python':
            self.df = pd.DataFrame(self.data_source)
        elif data_source_type == 'sql':
            pass

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
        self.df.rename(columns = columns, inplace=True)

