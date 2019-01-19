"""
Converts graph presented in dict to adjacency matrix

{'A': ['B', 'C'],
 'B': ['A', 'C', 'E'],
 'C': ['A', 'B', 'E', 'F'],
 'E': ['B', 'C'],
 'F': ['C']}

[[0, 1, 1, 0, 0],
 [1, 0, 1, 1, 0],
 [1, 1, 0, 1, 1],
 [0, 1, 1, 0, 0],
 [0, 0, 1, 0, 0]]
"""

from pprint import pprint

graph = {
    "A": ["B", "C"],
    "B": ["A", "C", "E"],
    "C": ["A", "B", "E", "F"],
    "E": ["B", "C"],
    "F": ["C"],
}


def graph_to_matrix(graph):
    matrix_elements = sorted(graph.keys())
    rows = len(matrix_elements)
    # allocate matrix size [row x row] with 0
    matrix = [[0] * rows for r in range(rows)]

    for i, row in enumerate(matrix_elements):
        for j, col in enumerate(matrix_elements):
            if col in graph[row]:
                matrix[i][j] = 1

    return matrix


pprint(graph)
matrix = graph_to_matrix(graph)
pprint(matrix)
