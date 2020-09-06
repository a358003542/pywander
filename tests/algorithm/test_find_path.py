#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_python_module.algorithm.graph.find_path import \
    find_shortest_path_dijkstra
from my_python_module.algorithm.graph.weighted_directed_graph import \
    WeightedDirectedGraph


def test_dijkstra():
    graph = WeightedDirectedGraph()
    graph.add_node('start')
    graph.add_edge(('start', 'a'))
    graph.add_edge(('start', 'b'))
    graph.add_edge(('a', 'end'))
    graph.add_edge(('b', 'end'))
    graph.set_edge_weight(('start', 'a'), 6)
    graph.set_edge_weight(('start', 'b'), 2)
    graph.set_edge_weight(('a', 'end'), 1)
    graph.set_edge_weight(('b', 'end'), 5)
    graph.add_edge(('b', 'a'))
    graph.set_edge_weight(('b', 'a'), 3)

    data = find_shortest_path_dijkstra(graph, 'start', 'end')

    assert data == ['start', 'b', 'a', 'end']
