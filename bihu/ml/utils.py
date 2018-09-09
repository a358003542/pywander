#!/usr/bin/env python
# -*-coding:utf-8-*-

import numpy as np



def data_normalize(data_set):
    min_vals = data_set.min(0)
    max_vals = data_set.max(0)
    ranges = max_vals - min_vals
    norm_data_set = np.zeros(np.shape(data_set))
    m = data_set.shape[0]
    norm_data_set = data_set - np.tile(min_vals, (m,1))/np.tile(ranges, (m,1))
    return norm_data_set, ranges, min_vals

def input_data(data, ranges, min_vals):
    return (data - min_vals)/ ranges

def restore_data(data_set, ranges, min_vals):
    old_data_set = (data_set * ranges) + min_vals
    return old_data_set