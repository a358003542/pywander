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
