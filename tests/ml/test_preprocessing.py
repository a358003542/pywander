#!/usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np

from ml.utils import scale, get_minmax_scaler, get_standard_scaler, inverse_scale
from ml.utils import DataFrameHandler

from ml.utils import encode, get_onehot_encoder, inverse_encode, get_label_encoder


def test_scale():
    data = np.array([
        [3, -1.5, 2, -5.4],
        [0, 4, -0.3, 2.1],
        [1, 3.3, -1.9, -4.3]
    ])

    df_handler = DataFrameHandler(data)
    df_handler.rename_columns({0: 'a', 1: 'b', 2: 'c', 3: 'd'})
    df = df_handler.get_df()

    std_scaler = get_standard_scaler()
    std_df = scale(std_scaler, df)
    assert np.allclose(std_df.values.mean(axis=0), np.zeros(std_df.shape))
    assert np.allclose(std_df.values.std(axis=0), np.ones(std_df.shape))

    minmax_scaler = get_minmax_scaler()
    minmax_df = scale(minmax_scaler, df)

    assert np.all(np.logical_and(minmax_df.values <= 1, minmax_df.values >= 0))

    df2 = inverse_scale(std_scaler, std_df)
    assert np.allclose(df.values, df2.values)


def test_label_encode():
    data = [['male', 10], ['female', 5], ['male', 1], ['male', 2]]
    nd = np.array(data)
    flatten_nd = nd.flatten()
    set_flatten_nd = set(flatten_nd)
    label_encoder = get_label_encoder()

    label_encode_nd = encode(label_encoder, flatten_nd, fit_data=list(set_flatten_nd))

    inversed_nd = inverse_encode(label_encoder, label_encode_nd)

    nd2 = inversed_nd.reshape(nd.shape)

    assert np.all(nd == nd2)


def test_onehot_encode():
    data = [['male', 10], ['female', 5], ['male', 1], ['male', 2]]
    nd = np.array(data, dtype=object)

    onehot_encoder = get_onehot_encoder()

    onehot_encode_nd = encode(onehot_encoder, data, fit_data=data)

    nd2 = inverse_encode(onehot_encoder, onehot_encode_nd)

    assert np.all(nd == nd2)
