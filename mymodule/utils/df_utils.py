#!/usr/bin/env python
# -*-coding:utf-8-*-


import pandas as pd
from loguru import logger

"""
pandas的DataFrame的一些便捷操作函数
"""


def combine_df(df_value, old_df):
    """
    输入ndarray值，然后根据给的老df的column列名来输出一个新的df
    :param df_value:
    :param old_df:
    :return:
    """
    new_df = pd.DataFrame(df_value, columns=old_df.columns)
    return new_df


def change_df_type(df, column_name, type):
    """
    输入 df column_name type
    将df的某个列的类型更改为某个type 比如float等

    :param df:
    :param column_name:
    :param type:
    :return:
    """
    df[column_name] = df[column_name].astype(type)


def rename_df_columns(df, columns):
    """
    重新设置列名
    """
    df.rename(columns=columns, inplace=True)


def rename_df_column_by_index(dataset, index, to):
    """
    将index column 名字修改为 to
    :param dataset:
    :param index:
    :param to:
    :return:
    """
    assert isinstance(index, int)

    d = {dataset.columns[index]: to}
    logger.debug(f'dataset column {dataset.columns[index]}  renamed to {to}')
    dataset.rename(columns=d, inplace=True)
    return dataset


def rename_df_column_by_name(dataset, name, to):
    """
    将某个column 名字修改为 to
    :param dataset:
    :param name:
    :param to:
    :return:
    """
    assert isinstance(name, str)
    assert isinstance(to, str)

    d = {name: to}
    logger.debug(f'dataset column {name} renamed to {to}')
    dataset.rename(columns=d, inplace=True)
    return dataset


def get_all_column(df, column_name, remove_duplicate=True):
    """
    获取一列所有的值 默认去重
    :param column_name:
    :param remove_duplicate:
    :return:
    """
    column_values = df[column_name].values
    if remove_duplicate:
        column_values = set(column_values)

    column_values = list(column_values)

    return column_values

import pandas as pd


class NoInputDataError(Exception):
    pass


class DataReader(object):
    """
    pandas的io接口做的很好

    read data source from
    - file
    - python  DataFrame dict ...
    - sql

    ## 读取数据函数  - 后续可能会扩展补充附加数据模式
    - 初始化读取数据 利用DataFrame的初始化 加载数据
    - load_from_txt
    - load_from_csv
    - load_from_excel
    - load_from_sql

    ## 获取数据
    - get_dataset 获取数据集 feature_columns 指定那些列为你想要的dataset
                  返回ndarray [[],[]]
    - get_labels  label_column 指定label的列的index 返回ndarrya []


    ## 列名控制 非必要
    - set_columns 设置列名
    - rename_column
    - renmae_columns

    """

    def __init__(self, data=None, **kwargs):
        if data is None:
            self.df = None
        else:
            self.df = pd.DataFrame(data, **kwargs)

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
        默认的column 可用 0 1 2 <int> 来引用
        :param origin_column_name:
        :param column_name:
        :return:
        """
        d = {}
        d[origin_column_name] = column_name
        self.df.rename(columns=d, inplace=True)

    def rename_columns(self, columns):
        self.df.rename(columns=columns, inplace=True)

    def get_df(self):
        return self.df

    def get_dataset(self, feature_columns):
        """
        输入 pandas 初步处理了的 df数据，针对knn进行数据准备
        :param df:
        :return:
        """
        if self.df is None:
            raise NoInputDataError

        dataset = self.df.iloc[:, feature_columns].values

        return dataset

    def get_labels(self, label_column):
        if self.df is None:
            raise NoInputDataError

        labels = self.df.iloc[:, label_column].values
        return labels
