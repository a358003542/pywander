#!/usr/bin/env python
# -*-coding:utf-8-*-


"""
针对有向图


"""
from sys import getrecursionlimit, setrecursionlimit
from collections import deque, defaultdict


def depth_first_search(graph, root, target):
    """
    Depth-first search.
    """

    recursionlimit = getrecursionlimit()
    setrecursionlimit(max(len(graph) * 2, recursionlimit))
    finded = False

    def dfs(node):
        """
        Depth-first search subfunction.
        """
        nonlocal finded
        if finded:
            return True

        for other in graph[node]:
            if other == target:
                spanning_tree[node].append(other)
                finded = True
                return True
            else:

                spanning_tree[node].append(other)
                dfs(other)
                print(spanning_tree)

    spanning_tree = defaultdict(list)


    dfs(root)
    setrecursionlimit(recursionlimit)
    return spanning_tree


def breadth_first_search(graph, root, target):
    """
    Breadth-first search.

    @type  graph: graph, digraph
    @param graph: Graph.

    @type  root: node
    @param root: Optional root node (will explore only root's connected component)

    @rtype:  tuple
    @return: A tuple containing a dictionary and a list.
        1. Generated spanning tree
        2. Graph's level-based ordering
    """

    def bfs():
        """
        Breadth-first search subfunction.
        """
        while (queue != []):
            node = queue.popleft()

            if (node not in spanning_tree):
                for other in graph[node]:
                    if other == target:
                        spanning_tree[node].append(other)
                        return True
                    else:
                        spanning_tree[node].append(other)
                        queue.extend(graph[node])

    queue = deque()  # Visiting queue
    spanning_tree = defaultdict(list)  # Visited

    queue.append(root)
    bfs()
    return spanning_tree



def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest


