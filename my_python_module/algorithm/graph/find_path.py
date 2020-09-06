#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_python_module.algorithm.graph.weighted_directed_graph import \
    WeightedDirectedGraph

import logging

logger = logging.getLogger(__name__)


def find_shortest_path_dijkstra(graph: WeightedDirectedGraph, start, end, ):
    processed = []
    costs = {}
    parents = {}  # 子节点---> 父节点

    # costs 初始化 直达的赋值，不能直达的赋无穷大
    #

    def init_costs(graph: WeightedDirectedGraph, start):
        nonlocal costs

        for node in graph.nodes():
            if node == start:
                pass
            elif node in graph.neighbors(start):
                costs[node] = graph.edge_weight((start, node))
            else:
                costs[node] = float("inf")

    def init_parents(graph: WeightedDirectedGraph, start):
        nonlocal parents

        for node in graph.nodes():
            if node == start:
                pass
            elif node in graph.neighbors(start):
                parents[node] = start
            else:
                parents[node] = None  # 与costs同步

    def find_lowest_cost_node(costs):
        """
        start - node the total cost
        always return the lowest cost node.
        :param costs:
        :return:
        """
        lowest_cost = float("inf")
        lowest_cost_node = None
        nonlocal processed

        for node, cost in costs.items():
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    def explain_parents(start, end, path=[]):
        nonlocal parents

        if start == end:
            path.append(start)
            return path
        else:
            for k, v in parents.items():
                if v == start:
                    path.append(start)
                    return explain_parents(k, end, path=path)

    init_costs(graph, start)
    init_parents(graph, start)

    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        for sub_node in graph.neighbors(node):
            new_cost = cost + graph.edge_weight((node, sub_node))
            if costs[sub_node] > new_cost:  # 需要更新
                costs[sub_node] = new_cost
                parents[sub_node] = node  # node -> sub_node

        processed.append(node)
        node = find_lowest_cost_node(costs)

    return explain_parents(start, end)


