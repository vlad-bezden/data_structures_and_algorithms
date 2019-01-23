"""
Find the shortest pass using Dijkstra's algorithm
"""

from pprint import pprint
from dataclasses import dataclass


INFINITY = float("inf")


@dataclass
class NodeInfo:
    parent: str
    distance: int

    def update(self, parent: str, distance: int):
        self.parent = parent
        self.distance = distance


def create_table(graph, origin):
    """Creates table of distances for each node"""
    table = {origin: NodeInfo(None, 0)}
    for k in (k for k in graph.keys() if k != origin):
        table[k] = NodeInfo(None, INFINITY)
    return table


def lowest_distance_node(processed, table):
    """Finds the lowest distance node.

    Lowest distance node hast to be processed next
    """
    lowest_distance = INFINITY
    lowest_node_distance = None
    for k, v in ((k, v) for k, v in table.items() if k not in processed):
        if v.distance < lowest_distance:
            lowest_distance = v.distance
            lowest_node_distance = k
    return lowest_node_distance


def shortest_path(graph, origin):
    """Creates table of shortest paths to all nodes from origin node"""
    table = create_table(graph, origin)
    visited_nodes = set()
    current_node = origin

    while current_node:
        # distance from origin node to current_node
        distance = table[current_node].distance
        # neighbors of current_node
        neighbors = graph[current_node]
        for k, v in neighbors.items():
            new_distance = distance + v
            if new_distance < table[k].distance:
                table[k].update(current_node, new_distance)
        visited_nodes.add(current_node)
        current_node = lowest_distance_node(visited_nodes, table)

    return table


def breadcrumb(target, table):
    """Trace shortest path from start to the target"""
    path = []
    while target:
        path.append(target)
        target = table[target].parent
    return reversed(path)


def print_shortest_path(target, table):
    path = breadcrumb(target, table)
    print(f"Shortest path to target '{target}' is {'->'.join(path)}")


def main():
    graph = {
        "A": {"B": 5, "D": 9, "E": 2},
        "B": {"A": 5, "C": 2},
        "C": {"B": 2, "D": 3},
        "D": {"A": 9, "F": 2, "C": 3},
        "E": {"A": 2, "F": 3},
        "F": {"E": 3, "D": 2},
    }
    result = shortest_path(graph, "A")
    pprint(result)
    print_shortest_path("D", result)


if __name__ == "__main__":
    main()
