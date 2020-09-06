#!/usr/bin/env python
# -*-coding:utf-8-*-


from my_python_module.algorithm.graph.directed_acyclic_graph import DirectedAcyclicGraph, NotAcyclicError
import logging
logging.basicConfig(level=logging.DEBUG)

import pytest

def test_dag():
    dag = DirectedAcyclicGraph()
    dag.add_edge(('a', 'b'))
    dag.add_edge(('a', 'c'))
    dag.add_edge(('b', 'e'))
    dag.add_edge(('e', 'f'))
    dag.add_edge(('f', 'c'))
    dag.add_edge(('c', 'g'))
    dag.add_edge(('g', 'h'))

    assert dag.sort()

    with pytest.raises(NotAcyclicError):
        dag.add_edge(('g','a'))

    print(dag)