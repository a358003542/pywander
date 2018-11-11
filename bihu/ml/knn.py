#!/usr/bin/env python
# -*-coding:utf-8-*-

import operator
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

from .exceptions import NoInputDataError
from .base import DataHandler
from .utils import data_normalize, input_data, restore_data


class KNN(DataHandler):
    def __init__(self, data_source=None, read_data_kwargs=None, k=5, test_size=0.1):
        super().__init__(data_source=data_source, read_data_kwargs=read_data_kwargs)

        self.k = k
        self.test_size = test_size

        self.data = None  # dataframe for knn algorithm needed data

        self.classifier = KNeighborsClassifier(n_neighbors=self.k)

    def prepare_data(self, picked_features, label_index=None):
        """
        输入 pandas 初步处理了的 df数据，针对knn进行数据准备
        :param df:
        :return:
        """
        if self.df is None:
            raise NoInputDataError

        if label_index is None:
            self.labels = self.df.labels.values
        else:
            self.labels = self.df.iloc[:, [label_index]].values

        self.data_set = self.df.iloc[:, picked_features].values

        self.new_data_set, self.ranges, self.min_vals = data_normalize(self.data_set)

    def train(self):
        self.classifier.fit(self.new_data_set, self.labels)

    def predict_one(self, data):
        res = self.classifier.predict(input_data([data], self.ranges, self.min_vals))
        return res[0]

    def predict_many(self, data):
        res = self.classifier.predict(input_data(data, self.ranges, self.min_vals))
        return res

    def test(self):
        self.train_data_set, self.test_data_set, self.train_labels, self.test_labels = train_test_split(
            self.new_data_set, self.labels, test_size=self.test_size)
        res = self.classifier.score(self.test_data_set, self.test_labels)
        return res
