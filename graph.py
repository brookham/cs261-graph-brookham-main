# Graph: An efficient graph.
# A graph implementation that uses an adjacency list to represent vertices and edges.
# Your implementation should pass the tests in test_graph.py.

# Brook Hamilton
# YOUR COLLABORATORS
# TIME SPENT: 

import functools

class Graph:
    def __init__(self):
        self.data = {}

    def adjacent(self, vert1, vert2):
        if self.data == None:
            return False
        
    def neighbors(self, vert):
        neighbor_lst = []
        
        return neighbor_lst

    def add_vertex(self, key):
        self.data[key] = []