#!/usr/bin/env python
# -*-coding:utf-8-*-


import pandas as pd


def combine_df(df_value, old_df):
    new_df = pd.DataFrame(df_value, columns=old_df.columns)
    return new_df
