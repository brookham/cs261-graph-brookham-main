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
        if vert1 in self.data:
            return vert2 in self.data[vert1]



        
    def neighbors(self, vert):
        if len(self.data) <= 1:
            return []

    def add_vertex(self, key):
        if key in self.data:
            pass
        else:
            self.data[key] = []

    def remove_vertex(self, key):
        if key not in self.data:
            pass
        else:
            del self.data[key]

    def add_edge(self, vert1, vert2):
        if not vert1 or vert2 in self.data:
            pass

    def remove_edge(self, vert1, vert2):
        if not vert1 or vert2 in self.data:
            pass