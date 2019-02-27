#!/usr/bin/env python
# -*-coding:utf-8-*-


from ml.knn import KNN


def test_knn():
    test_txt = 'tests\ml\datingTestSet.txt'

    read_data_kwargs = {
        'sep': '\t',
        'header': None
    }
    knn_handler = KNN()
    knn_handler.load_from_csv(test_txt, **read_data_kwargs)

    knn_handler.rename_column(origin_column_name=3, column_name='labels')

    knn_handler.prepare_data(picked_features=[0, 1, 2])

    knn_handler.train()

    assert knn_handler.predict_one([[14254, 5.9, 1.6]]) == 2

    assert knn_handler.test() > 0.5
