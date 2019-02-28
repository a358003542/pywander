#!/usr/bin/env python
# -*-coding:utf-8-*-


import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler

from sklearn.preprocessing import normalize as sk_normalize
from sklearn.preprocessing import binarize as sk_binarize

from utils import combine_df

"""

- scale 缩放操作 (缩放器 df) 返回df
- inverse_scale 反向缩放操作 (缩放器 df) 返回df
- normalize(df, norm='l1') 归一化
- binarize 二值化 阈值默认为0

- encode 编码
- inverse_encode 反编码 

### 缩放器
- z-score标准化 get_standard_scaler
- minmax缩放 get_minmax_scaler


"""

from sklearn.preprocessing import OneHotEncoder

"""

one hot encoding
"""

from sklearn.preprocessing import LabelEncoder

"""

LabelEncoder  标记编码
"""


def scale(scaler, df):
    """
    缩放操作
    :param scaler:
    :param df:
    :return:
    """
    if isinstance(df, pd.DataFrame):
        df_value = scaler.fit_transform(df)
        new_df = combine_df(df_value, df)
        return new_df
    elif isinstance(df, np.ndarray):
        df_value = scaler.fit_transform(df)
        return df_value


def inverse_scale(scaler, df):
    """
    反向缩放操作 - 反向缩放的有：

    - minmax
    - stand

    :param scaler:
    :param df:
    :return:
    """
    if isinstance(df, pd.DataFrame):
        df_value = scaler.inverse_transform(df)
        new_df = combine_df(df_value, df)
        return new_df
    elif isinstance(df, np.ndarray):
        df_value = scaler.inverse_transform(df)
        return df_value


def normalize(df, norm='l1'):
    """
    归一化 norm选项有 l1 范数 和 l2 范数 选项
    :param df:
    :param norm:
    :return:
    """
    if isinstance(df, pd.DataFrame):
        df_value = sk_normalize(df, norm=norm)
        new_df = combine_df(df_value, df)
        return new_df
    elif isinstance(df, np.ndarray):
        df_value = sk_normalize(df, norm=norm)
        return df_value


def binarize(df, threshold=0):
    """
    二值化 给定阈值默认为0, 然后根据阈值来返回0和1
    :param df:
    :param threshold:
    :return:
    """
    if isinstance(df, pd.DataFrame):
        df_value = sk_binarize(df, threshold=threshold)
        new_df = combine_df(df_value, df)
        return new_df
    elif isinstance(df, np.ndarray):
        df_value = sk_binarize(df, threshold=threshold)
        return df_value


def encode(encoder, df, fit_data=None):
    """
    编码
    :param encoder:
    :param df:
    :return:
    """
    if fit_data is not None:
        encoder.fit(fit_data)

    if isinstance(encoder, OneHotEncoder):
        df_value = encoder.transform(df).toarray()
        return df_value
    elif isinstance(encoder, LabelEncoder):
        df_value = encoder.transform(df)
        return df_value


def inverse_encode(encoder, df):
    """
    反向编码

    可以反向编码的有：
    - onehot
    - label

    :param encoder:
    :param df:
    :return:
    """

    df_value = encoder.inverse_transform(df)
    return df_value


def get_standard_scaler():
    """
    均值移除 或者 z-score标准化
    :param scaler:
    :param df:
    :return:
    """
    return StandardScaler()


def get_minmax_scaler(feature_range=(0, 1)):
    """
    范围缩放，同样缩放到0-1，所以也叫做 0-1缩放
    :param scaler:
    :param df:
    :return:
    """
    scaler = MinMaxScaler(feature_range=feature_range)
    return scaler
