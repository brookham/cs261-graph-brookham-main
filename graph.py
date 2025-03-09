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
        if vert in self.data:
            return self.data[vert]
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
            for vert in self.data:
                if key in self.data[vert]:
                    self.data[vert].remove(key)
            return self.data

    def add_edge(self, vert1, vert2):
        if not vert1 or vert2 in self.data:
            pass
        if vert1 and vert2 in self.data:
            self.data[vert1].append(vert2)
            self.data[vert2].append(vert1)

    def remove_edge(self, vert1, vert2):
        if not vert1 or vert2 in self.data:
            pass