#!/usr/bin/env python
# -*-coding:utf-8-*-


from bihu.algorithms.graph.find_path import breadth_first_search, find_shortest_path,depth_first_search


def test_bfs():
    graph = {
        'a': ['b', 'c'],
        'b': ['e', 'd'],
        'd': ['f'],
        'c': [],
        'e': [],
        'f': []
    }

    data = breadth_first_search(graph, root='a', target='f')
    print(data)


    graph = {
        'you': ['alice','bob','claire'],
        'bob': ['anuj','peggy'],
        'alice':['peggy'],
        'claire': ['thom','jonny'],
        'anuj':[],
        'peggy':[],
        'thom':[],
        'jonny':[]
    }
    data = breadth_first_search(graph, root='you',target='anuj')

    data = find_shortest_path(data, start='you',end='anuj')
    assert data == ['you', 'bob', 'anuj']

    data = breadth_first_search(graph, root='you',target='peggy')
    data = find_shortest_path(data, start='you',end='peggy')
    assert data == ['you', 'alice', 'peggy'] or data == ['you','bob','peggy']


def test_dfs():
    graph = {
        'you': ['alice', 'bob', 'claire'],
        'bob': ['anuj', 'peggy'],
        'alice': ['peggy'],
        'claire': ['thom', 'jonny'],
        'anuj': [],
        'peggy': [],
        'thom': [],
        'jonny': []
    }
    data = depth_first_search(graph, root='you', target='anuj')

    print(data)

