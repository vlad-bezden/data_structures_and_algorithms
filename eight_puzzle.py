""" 8 Puzzle
    https://py.checkio.org/en/mission/8-puzzle/

    8 puzzle is a sliding puzzle that consists of a frame of randomly ordered,
    numbered square tiles with one missing tile.
    The object of the puzzle is to place the tiles in the right order
    (see picture) by using sliding moves to utilize the empty space.
    You can read more about this kind of puzzle on Wikipedia.

    Our puzzle is presented as a 3x3 matrix with numbers from 1 to 8.
    Zero is the empty cell. You can "move" the empty cell in four directions:
    up--"U", down--"D", left--"L", and right--"R".
    You need to return a sequence of moves to solve the puzzle.
    The solution is presented as string of symbols ("UDLR") describing your moves.

    Input: A matrix with numbers from 1 to 8 as a list of lists with integers.

    Output: The route of the empty cell as a string.

    Precondition:
    len(puzzle) == 3
    all(len(row) == 3 for row in puzzle)
"""

from __future__ import annotations
from heapq import heappush, heappop
from copy import deepcopy
from typing import List, Tuple, Dict

Puzzle = List[List[int]]
Coordinate = Tuple[int, int]

GOAL = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
SIZE = len(GOAL)
MOVES: Dict[str, Coordinate] = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}


def create_node(node: Node, coordinate: Coordinate, direction) -> Node:
    """Creates node based on move existing node to new coordinate"""
    new_state = deepcopy(node.state)
    new_state[node.zero[0]][node.zero[1]] = node.value(coordinate)
    new_state[coordinate[0]][coordinate[1]] = 0
    new_node = Node(node, new_state, node.path + direction, node.cost + 1)
    return new_node


def get_moves(node: Node) -> List[Node]:
    """Gets all legal moves.
        Legal move is the one that doesn't cross boundary: 0 <= i < SIZE
    """
    neighbors = []
    for direction, value in MOVES.items():
        neighbor: Coordinate = tuple(map(sum, zip(node.zero, value)))
        if all(0 <= i < SIZE for i in neighbor):
            new_node = create_node(node, neighbor, direction)
            neighbors.append(new_node)
    return neighbors


class Node:
    """Current state representation of the board and it's value"""

    def __init__(self, parent: Node, state: Puzzle, path: str, cost: int) -> None:
        self.parent = parent
        self.state = state
        # g(n) - number of steps taken to the current state
        self.cost = cost
        # h(n) - estimated distance to goal
        self.heuristic = self._calc_heuristic_cost()
        self.path = path
        self.zero = self._find_zero()

    def _calc_heuristic_cost(self) -> int:
        """Current puzzle heuristic cost using Manhatten distance."""
        h_val = 0
        for i, row in enumerate(self.state):
            for j, v in enumerate(row):
                if self.value((i, j)) != GOAL[i][j]:
                    x, y = divmod(v - 1, SIZE)
                    h_val += abs(x - i) + abs(y - j)
        return h_val

    def _find_zero(self) -> Coordinate:
        """Finds coordinates of the empty cell (0)"""
        for x, row in enumerate(self.state):
            for y, v in enumerate(row):
                if v == 0:
                    return x, y
        raise ValueError("There is no 0 found in the Puzzle")

    def value(self, coordinate: Coordinate) -> int:
        """Returns value of the coordinate (x, y)."""
        return self.state[coordinate[0]][coordinate[1]]

    @property
    def _total_cost(self) -> int:
        """Returns cost + heuristic cost"""
        return self.cost + self.heuristic

    def __lt__(self, other: "Node") -> bool:
        return self._total_cost < other._total_cost

    def __repr__(self) -> str:
        return f"Node({self.state}, {self.path}, {self.cost})"

    def __str__(self):
        path = self.path
        cost = self.cost
        heuristic = self.heuristic
        total_cost = self._total_cost
        return f"{path=}, \n{cost=}, \n{heuristic=}, \n{total_cost=}, \n" + "\n".join(
            map(str, self.state)
        )


class PriorityQueue:
    def __init__(self) -> None:
        self._container: List[Node] = []

    @property
    def empty(self) -> bool:
        return not self._container

    def push(self, item: Node) -> None:
        heappush(self._container, item)

    def pop(self) -> Node:
        return heappop(self._container)

    def __repr__(self) -> str:
        return repr(self._container)


def a_star(initial: Puzzle) -> str:
    to_visit = PriorityQueue()
    to_visit.push(Node(None, initial, "", 0))
    visited = []

    while to_visit:
        current = to_visit.pop()
        visited.append(current.state)
        # check if goal is met.
        if current.state == GOAL:
            print(f"Number of tries: {len(visited)}.")
            return current

        # check for all moves that are not visited yet and add them
        # to the queue
        for c in (c for c in get_moves(current) if c.state not in visited):
            to_visit.push(c)
    raise Exception("Could not find solution")


def print_states(node):
    stack = []
    print("\nSolutions:")
    while node:
        stack.append(node)
        node = node.parent

    while stack and (node := stack.pop()):
        print(node, "\n")


def checkio(puzzle: Puzzle) -> str:
    """Entry function for solving a puzzle"""
    # find solution based on A* algorithm
    result = a_star(puzzle)
    print(f"Final solution: {result.path} \nNumber of moves {len(result.path)}")
    print_states(result)
    return result.path


if __name__ == "__main__":

    def check_solution(func, puzzle):
        size = len(puzzle)
        route = func([row[:] for row in puzzle])
        goal = GOAL
        x = y = None
        for i, row in enumerate(puzzle):
            if 0 in row:
                x, y = i, row.index(0)
                break
        for ch in route:
            swap_x, swap_y = x + MOVES[ch][0], y + MOVES[ch][1]
            if 0 <= swap_x < size and 0 <= swap_y < size:
                puzzle[x][y], puzzle[swap_x][swap_y] = puzzle[swap_x][swap_y], 0
                x, y = swap_x, swap_y
        if puzzle == goal:
            return True
        else:
            print("Puzzle is not solved")
            return False

    assert check_solution(checkio, [[1, 2, 3], [4, 6, 8], [7, 5, 0]]), "1st example"
    assert check_solution(checkio, [[7, 3, 5], [4, 8, 6], [1, 2, 0]]), "2nd example"
    print("PASSED!!!")
