## algorithm
some algorithm implemented on python.

### graph
#### Graph 
the general Graph class


```
    graph_data2 = {
        'you': ['alice', 'bob', 'claire'],
        'bob': ['anuj', 'peggy'],
        'alice': ['peggy'],
        'claire': ['thom', 'jonny'],
        'anuj': [],
        'peggy': [],
        'thom': [],
        'jonny': []
    }
    graph2 = DirectedGraph(graph_data2)

    graph2_shortest_path = graph2.dfs_shortest_path(start='you', end='anuj')
    assert graph2_shortest_path == ['you', 'bob', 'anuj']
    graph2_shortest_path2 = graph2.dfs_shortest_path(start='you', end='peggy')
    assert graph2_shortest_path2 == ['you', 'alice', 'peggy'] \
           or graph2_shortest_path2 == ['you', 'bob', 'peggy']

    graph2_shortest_path3 = graph2.bfs_shortest_path(start='you', end='anuj')
    assert graph2_shortest_path3 == ['you', 'bob', 'anuj']
```

##### order
```
    def order(self):
        """
        Return the order of self, this is defined as the number of nodes in the graph.
        """
```
##### bfs_shortest_path
```
    def bfs_shortest_path(self, start, end):
```

##### dfs_shortest_path
```
    def dfs_shortest_path(self, start, end):
```

#### DirectedGraph
```
    dg = DirectedGraph()
    dg.add_edge(("a", "d"))
    dg.add_edge(("d", "c"))
    dg.add_edge(("c", "b"))
    dg.add_edge(("c", "e"))
    dg.add_edge(("c", "c"))
    dg.add_edge(('b', 'f'))

    assert dg.order() == 6
    assert dg.has_node('a')
    assert dg.has_edge(('a', 'd'))

    dg.del_edge(('c', 'e'))
    assert not dg.has_edge(('c', 'e'))

    dg.del_node('c')

    assert not dg.has_node('c')
    assert dg.order() == 5

```

#### UndirectedGraph


### tree
#### Tree
```python
class Tree(object):
    """
    the brother nodes can not have the same name.
    """

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.children = []
```

```

def test_tree():
    tree = Tree("a")
    tree.insert_child("a", "b")
    tree.insert_child("a", "c")
    tree.insert_child("b", "d")
    tree.insert_child("b", "e")
    tree.insert_child("b", "f")
    tree.insert_child("c", "g")
    tree.insert_child("c", "h")
    tree.insert_child("d", "i")
    tree.insert_child("e", "j")

    assert tree.has_node('c')
    assert tree['c'].has_child('g')

    assert tree['a'].level == 1
    assert tree['d'].level == 3

    assert [i.name for i in tree.shortest_path_to('h')] == ['a', 'c', 'h']

```
#### BinarySearchTree
```
tree = BinarySearchTree(8)

    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)

    assert tree.find(4)
    assert not tree.find(50)
```
### binary_search
#### binary_search_func
```python

def binary_search_func(seq, target, func=lambda x: x, round_n=4, approx=True):
    """
    use binary search to solve f(x) = target problem, if the function is a
    monotonic function.

    seq  list or tuple
    target found target in which case is the f(x) = target
    func the monotonic function
    round_n accurate to how many decimal point
    approx the approx mode
    if approx=True found target or some nearly target, return it's index
    if approx=False  found target index otherwise return -1
    """
```

#### binary_search
```python
def binary_search(seq, target):
    """
    use the bisect_left.
    """
```
#### binary_insert
```python
def binary_insert(seq, target):
    """
    use the insort_left
    """
```

### quick_sort
#### quick_sort
```python
def quick_sort(seq):
    """
    10000 random number seq ：
    select_sort use time 3.0919713973999023
    quick sort use time 0.024930477142333984

    """
```

### select_sort
#### select_sort
```
def select_sort(seq):
```