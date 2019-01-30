"""
Adjacency Matrices directed graph
"""
from collections import defaultdict


class DirectedGraphAM:
    def __init__(self):
        self.vertices = defaultdict(dict)

    def add_edge(self, u, v, weight):
        self.vertices[u][v] = weight

    def neighbors(self, u):
        for item in self.vertices[u].items():
            yield item

    def __repr__(self):
        """Representation of graph."""
        rep = "graph:["
        for k, v in self.vertices.items():
            rep += f"{str(k)}: {', '.join(map(str, v.items()))}"
        return rep + "]"


if __name__ == "__main__":
    d = DirectedGraphAM()
    d.add_edge(0, 2, 99)
    print(d)
    d.add_edge(0, 3, 88)
    print(d)
    d.add_edge(0, 2, 777)
    print(d)
    for i in d.neighbors(0):
        print(i)
