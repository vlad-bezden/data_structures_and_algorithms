"""
You get an input as list of list List[List[Int]]
The input can have values 0, 1 and only one valuse is 7.
You always starts from top left cornet of the matrix and you can move on 1 only,
not on 0.
Most left corner with coordinates 0, 0 always has 1

Find minimum number of stept from left top cornet to the number 7
"""

from typing import List
from queue import deque
from collections import namedtuple
from functools import partial

Maze = List[List[int]]

Point = namedtuple("Point", ["x", "y"])

MOVES = [
    ("N", Point(-1, 0)),
    ("E", Point(0, 1)),
    ("S", Point(1, 0)),
    ("W", Point(0, -1)),
]
START = Point(0, 0)
FINAL_VALUE = 7


def is_inside(point: Point, width: int, height: int) -> bool:
    """Checks if point/coordinate inside of box"""

    return (
        False
        if (point.x < 0 or point.x >= height or point.y < 0 or point.y >= width)
        else True
    )


def new_point(left: Point, right: Point) -> Point:
    """Add movement to the current point"""
    return Point(left.x + right.x, left.y + right.y)


def bfs_find(maze: Maze) -> str:
    width = len(maze[0])
    height = len(maze)
    is_inside_ = partial(is_inside, width=width, height=height)
    visited = set()
    current = ("", START)
    queue = deque([current])

    while queue:
        path, current = queue.pop()
        if current in visited:
            continue
        if maze[current.x][current.y] == FINAL_VALUE:
            return path
        visited.add(current)
        for direction, offset in MOVES:
            neighbor = new_point(current, offset)
            if is_inside_(neighbor) and maze[neighbor.x][neighbor.y] >= 1:
                queue.append((path + direction, neighbor))

    return "NOT FOUND!"


if __name__ == "__main__":
    maze = [
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
    path = bfs_find(maze)
    print(f"Path: {path}")
