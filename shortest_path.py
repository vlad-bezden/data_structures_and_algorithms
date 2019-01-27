"""
Find the shortest pass using Dijkstra's algorithm
"""

import sys
from pprint import pprint
from dataclasses import dataclass
from typing import Dict, TypeVar, Optional, Iterator, Set

INFINITY = sys.maxsize

Path = Dict[str, int]
Graph = Dict[str, Path]
Node = TypeVar("Node", bound="NodeInfo")
Table = Dict[str, Node]


@dataclass
class NodeInfo:
    parent: Optional[str] = None
    distance: int = INFINITY

    def update(self, parent: Optional[str], distance: int) -> None:
        self.parent = parent
        self.distance = distance


def create_table(graph: Graph, origin: str) -> Table:
    """Creates table of distances for each node"""
    return {k: NodeInfo(k, 0 if k == origin else INFINITY) for k in graph.keys()}


def lowest_distance_node(processed: Set[str], table: Table) -> Optional[str]:
    """Finds the lowest distance node.

    Lowest distance node hast to be processed next
    """
    return min(
        ((k, v) for k, v in table.items() if k not in processed),
        key=lambda i: i[1].distance,
        default=(None,),
    )[0]


def shortest_path(graph: Graph, origin: str) -> Table:
    """Creates table of shortest paths to all nodes from origin node"""
    table = create_table(graph, origin)
    visited_nodes = set()
    current_node: Optional[str] = origin

    while current_node:
        # distance from origin node to current_node
        distance = table[current_node].distance
        # neighbors of current_node
        for k, v in graph[current_node].items():
            new_distance = distance + v
            if new_distance < table[k].distance:
                table[k].update(current_node, new_distance)
        visited_nodes.add(current_node)
        current_node = lowest_distance_node(visited_nodes, table)

    return table


def breadcrumb(target: str, table: Table) -> Iterator[str]:
    """Trace shortest path from start to the target"""
    path = []
    while target:
        path.append(target)
        target = table[target].parent
    return reversed(path)


def print_shortest_path(target: str, table: Table) -> None:
    path = breadcrumb(target, table)
    print(f"Shortest path to target '{target}' is {'->'.join(path)}")


def main() -> None:
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
    assert result["C"].distance == 7
    assert result["D"].distance == 7
    assert result["F"].distance == 5

    # another example from enki's app
    graph = {
        "A": {"B": 10, "C": 5, "D": 20, "E": 18},
        "B": {"A": 10, "D": 5},
        "C": {"A": 5, "D": 3},
        "D": {"A": 20, "E": 2},
        "E": {"A": 18, "D": 2},
    }
    result = shortest_path(graph, "A")
    pprint(result)
    print_shortest_path("E", result)
    assert result["B"].distance == 10
    assert result["C"].distance == 5
    assert result["D"].distance == 8
    assert result["E"].distance == 10


if __name__ == "__main__":
    main()
