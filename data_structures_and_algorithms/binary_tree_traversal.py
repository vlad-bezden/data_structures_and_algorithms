"""Different types of traversing tree.

        4
       /  \
      2     8
     / \   / \
    1   3 5  10

"""

from __future__ import annotations
from collections import deque
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    left: Node = None
    right: Node = None

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


@dataclass
class Tree:
    root: Node

    def breadth_first(self):
        """Breadth First Search (BFS)."""
        queue = deque([self.root])
        visited = []

        while queue:
            current = queue.pop()
            if left := current.left:
                queue.appendleft(left)
            if right := current.right:
                queue.appendleft(right)
            visited.append(current)
        print("->".join(map(str, visited)))

    def depth_first(self):
        """Depth First Search (DFS)."""
        stack = deque([self.root])
        visited = []

        while stack:
            current = stack.pop()
            if right := current.right:
                stack.append(right)
            if left := current.left:
                stack.append(left)
            visited.append(current)
        print("->".join(map(str, visited)))

    def _in_order(self, parent):
        if parent:
            self._in_order(parent.left)
            print(parent, end="->")
            self._in_order(parent.right)

    def in_order(self):
        """Inorder traversal using recursion."""
        self._in_order(self.root)
        print()

    def in_order2(self):
        """Inorder traversal without recursion."""
        stack = []
        current = self.root
        visited = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                visited.append(current := stack.pop())
                current = current.right
            else:
                break
        print("->".join(map(str, visited)))


if __name__ == "__main__":
    node_1 = Node(1)
    node_3 = Node(3)
    node_5 = Node(5)
    node_10 = Node(10)
    node_2 = Node(2, node_1, node_3)
    node_8 = Node(8, node_5, node_10)
    node_4 = Node(4, node_2, node_8)

    tree = Tree(node_4)
    print("BFS")
    tree.breadth_first()
    print("DFS")
    tree.depth_first()
    print("Inorder using recursion")
    tree.in_order()
    print("Inorder withou recursion")
    tree.in_order2()
