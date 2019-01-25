"""
You get an input as list of list List[List[Int]]
The input can have values 0, 1 and only one valuse is 7.
You always starts from top left cornet of the matrix and you can move on 1 only,
not on 0.
Most left corner with coordinates 0, 0 always has 1

Find minimum number of stept from left top cornet to the number 7
"""

from __future__ import annotations
from typing import List, Set
from collections import namedtuple, deque


Map = List[List[int]]
Size = namedtuple("Size", ["width", "heigth"])
Point = namedtuple("Point", ["x", "y"])

MOVES = [
    ("N", Point(-1, 0)),
    ("E", Point(0, 1)),
    ("S", Point(1, 0)),
    ("W", Point(0, -1)),
]
START = Point(0, 0)
FINAL_VALUE = 7


def add_points(first: Point, second: Point) -> Point:
    """Adds two points and creates new point"""
    return Point(first.x + second.x, first.y + second.y)


class Maze:
    def __init__(self, map: Map) -> None:
        self.map = map
        self.size = Size(len(map[0]), len(map))

    def valid_point(self, point: Point) -> bool:
        """Checks if point inside of the map and it's final or path value"""
        return (
            0 <= point.x < self.size.heigth
            and 0 <= point.y < self.size.width
            and self.value(point) in [1, FINAL_VALUE]
        )

    def value(self, point: Point) -> int:
        """Value on the map"""
        return self.map[point.x][point.y]

    def bfs_find(self):
        """Searches for shortest path using Breadth First Search (BFS)"""
        visited: Set[Point] = set()
        queue = deque([("", START)])

        while queue:
            path, current = queue.pop()
            if self.value(current) == FINAL_VALUE:
                return path
            if current in visited:
                continue
            for dir, point in MOVES:
                new_point = add_points(current, point)
                if self.valid_point(new_point):
                    queue.appendleft((path + dir, new_point))
            visited.add(current)
        return "NOT FOUND!!!"


if __name__ == "__main__":
    map = [
        [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 1, 1, 0, 1, 0],
        [1, 0, 1, 1, 1, 1, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0, 1, 0, 0, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 1, 0, 0, 7],
    ]
    maze = Maze(map)
    path = maze.bfs_find()
    print(f"Path: {path}")
    # 8S -> 2E -> 1N -> 7E -> 4S
    assert path == "SSSSSSSSEENEEEEEEESSSS"
    print("Done!!!")
