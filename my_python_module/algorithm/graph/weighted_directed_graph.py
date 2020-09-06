#!/usr/bin/env python
# -*-coding:utf-8-*-
from my_python_module.algorithm.graph.directed_graph import DirectedGraph
from my_python_module.exceptions import AdditionError


class WeightedDirectedGraph(DirectedGraph):
    """
     带权重的有向图， 权重作为 weight 属性值而存在。

     {
         'a': {'b':{},'z':{}} 只记录指向
     }
     """
    DIRECTED = True
    WEIGHT_ATTRIBUTE_NAME = "weight"
    DEFAULT_WEIGHT = 1

    def neighbors(self, node):
        """
        Return all nodes that are incident to the given node.
        """
        return list(self.graph_dict[node].keys())

    def add_node(self, node):
        """
        Add given node to the graph.

        @attention: While nodes can be of any type, it's strongly recommended to use only
        numbers and single-line strings as node identifiers if you intend to use write().

        @type  node: node
        @param node: Node identifier.

        """

        if (node not in self.graph_dict):
            self.graph_dict[node] = {}
        else:
            raise AdditionError("Node {0} already in digraph".format(node))

    def add_edge(self, edge):
        """
        Add an directed edge to the graph connecting two nodes.

        """
        u, v = edge
        for n in [u, v]:
            if not n in self.graph_dict:
                self.add_node(n)

        if v in self.graph_dict[u] and u in self.graph_dict[v]:
            raise AdditionError("Edge (%s, %s) already in digraph" % (u, v))
        else:
            self.graph_dict[u][v] = {}

    def del_edge(self, edge):
        """
        Remove an directed edge from the graph.

        @type  edge: tuple
        @param edge: Edge.
        """
        u, v = edge
        if v in self.graph_dict[u]:
            self.graph_dict[u].pop(v)

    def edge_attr(self, edge, key):
        u, v = edge
        return self.graph_dict[u][v].get(key)

    def set_edge_attr(self, edge, key, value):
        u, v = edge
        self.graph_dict[u][v][key] = value

    def edge_weight(self, edge):
        return self.edge_attr(edge, self.WEIGHT_ATTRIBUTE_NAME)

    def set_edge_weight(self, edge, weight=DEFAULT_WEIGHT):
        self.set_edge_attr(edge, self.WEIGHT_ATTRIBUTE_NAME, weight)