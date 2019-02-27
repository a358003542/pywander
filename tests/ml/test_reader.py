#!/usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np

from ml.utils import DataFrameHandler


def test_df_handler():
    data = np.array([
        [3, -1.5, 2, -5.4],
        [0, 4, -0.3, 2.1],
        [1, 3.3, -1.9, -4.3]
    ])

    df_handler = DataFrameHandler(data)
    df_handler.rename_columns({0: 'a', 1: 'b', 2: 'c', 3: 'd'})
    df = df_handler.get_df()

    assert np.all(df.columns == ['a', 'b', 'c', 'd'])
    assert np.all(df.values == data)
