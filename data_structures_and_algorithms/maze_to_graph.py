"""Converts maze to graph/dictionary with direction"""

from typing import List, Dict, Tuple
from collections import namedtuple

# regular point with x/row, y/column coordinates
Point = namedtuple("Point", ["row", "col"])
# point that also has direction
DirPoint = namedtuple("DirPoint", ["path", "point"])

Maze = List[List[int]]
Graph = Dict[Point, List[Tuple[str, Point]]]


WALL = 1
PATH = 0


def maze_to_graph(maze: Maze) -> Graph:
    """Converts maze to graph with direction"""

    rows = len(maze)
    cols = len(maze[0])

    # get all PATH points
    graph = {
        Point(row, col): []
        for row in range(rows)
        for col in range(cols)
        if maze[row][col] == PATH
    }

    for point in graph:
        # check bellow
        if point.row < rows - 1:
            point_bellow = Point(point.row + 1, point.col)
            if graph.get(point_bellow) is not None:
                graph[point].append(DirPoint("S", point_bellow))
                graph[point_bellow].append(DirPoint("N", point))
        # check point to the right
        if point.col < cols - 1:
            point_right = Point(point.row, point.col + 1)
            if graph.get(point_right) is not None:
                graph[point].append(DirPoint("E", point_right))
                graph[point_right].append(DirPoint("W", point))

    return graph


def bfs_search(graph, start, end):
    from collections import deque
    visited = set()
    queue = deque([("", start)])

    while queue:
        path, current = queue.popleft()
        if current == end:
            return path
        if current in visited:
            continue
        visited.add(current)
        for direction, neightbor in graph[current]:
            queue.append((path + direction, neightbor))
    return "NOT FOUND!"

if __name__ == "__main__":
    maze = [[0, 0, 1], [1, 0, 1], [1, 0, 0]]
    graph = maze_to_graph(maze)
    print("\n", graph)

    maze = [
        [0, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 0, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    ]
    graph = maze_to_graph(maze)

    result = bfs_search(graph, Point(0, 0), Point(len(maze) - 1, len(maze[0]) - 1))
    print(result)
