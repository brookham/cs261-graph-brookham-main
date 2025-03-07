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
        if len(self.data) <= 1:
            return False
        
    def neighbors(self, vert):
        neighbor_lst = []
        if len(self.data) <= 1:
            return neighbor_lst

    def add_vertex(self, key):
        if key in self.data:
            pass
        else:
            self.data[key] = []

    def remove_vertex(self, key):
        pass

    def add_edge(self, vert1, vert2):
        pass

    def remove_edge(self, vert1, vert2):
        pass