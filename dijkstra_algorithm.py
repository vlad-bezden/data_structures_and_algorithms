"""
Dijkstra's task solution from enki's application
'comp.sci. data strucutures and algorithms'
"""

import sys
from dataclasses import dataclass
from pprint import pprint

INFINITY = sys.maxsize


def graph_to_table(graph, start):
    return {k: Node(None, 0 if k == start else INFINITY) for k in graph}


def next_to_process(table, visited):
    return min(
        ((k, v) for k, v in table.items()), key=lambda i: i[1].value, default=(None, 0)
    )[0]


@dataclass
class Node:
    parent: str = None
    value: int = INFINITY

    def update(self, parent, value):
        self.parent = parent
        self.value = value


def calc(graph, start):
    visited = set()
    current = start
    table = graph_to_table(graph, start)

    while current:
        current_value = table[current].value
        for k, v in graph[current].items():
            new_value = current_value + v
            if new_value < table[k].value:
                table[k].update(current, new_value)
        visited.add(current)
        current = next_to_process(table, visited)

    return table


def main():
    start = "A"
    graph = {
        "A": {"B": 10, "C": 5, "D": 20, "E": 18},
        "B": {"A": 10, "D": 5},
        "C": {"A": 5, "D": 3},
        "D": {"A": 20, "E": 2},
        "E": {"A": 18, "D": 2},
    }
    table = calc(graph, start)
    pprint(table)
    assert table["A"] == Node(None, 0)
    assert table["B"] == Node("A", 10)
    assert table["C"] == Node("A", 5)
    assert table["D"] == Node("C", 8)
    assert table["E"] == Node("D", 10)

    graph = {
        "A": {"B": 5, "D": 9, "E": 2},
        "B": {"A": 5, "C": 2},
        "C": {"B": 2, "D": 3},
        "D": {"A": 9, "C": 3, "F": 2},
        "E": {"A": 2, "F": 3},
        "F": {"E": 3, "D": 2},
    }
    table = calc(graph, start)
    print("\n")
    pprint(table)

    assert table["A"] == Node(None, 0)
    assert table["B"] == Node("A", 5)
    assert table["C"] == Node("B", 7)
    assert table["D"] == Node("F", 7)
    assert table["E"] == Node("A", 2)
    assert table["F"] == Node("E", 5)


if __name__ == "__main__":
    main()
    print("DONE!!!")
