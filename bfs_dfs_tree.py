"""
Traverse graph using BFS, and DFS
"""

from collections import deque
from typing import List, Dict
from pprint import pprint


Graph = Dict[str, List[str]]


def bfs(graph: Graph, root: str) -> List[str]:
    """Breadth First Search (BFS) implementation"""

    queue = deque([root])
    visited = []

    while queue:
        current = queue.pop()
        if current not in visited:
            neighbors = graph[current]
            queue.extendleft(neighbors)
            visited.append(current)

    return visited


def dfs(graph: Graph, root: str) -> List[str]:
    """Depth First Search (DFS) implementation"""

    stack = deque([root])
    visited = []

    while stack:
        current = stack.pop()
        if current not in visited:
            neighbors = graph[current]
            stack.extend(neighbors)
            visited.append(current)

    return visited


def main():
    graph = {
        "A": ["B", "G", "D"],
        "B": ["A", "F", "E"],
        "C": ["F", "H"],
        "D": ["F", "A"],
        "E": ["B", "G"],
        "F": ["B", "D", "C"],
        "G": ["A", "E"],
        "H": ["C"],
    }
    print("Graph")
    pprint(graph)
    print("Using BFS")
    pprint(bfs(graph, "A"))
    print("using DFS")
    pprint(dfs(graph, "A"))


if __name__ == "__main__":
    main()
