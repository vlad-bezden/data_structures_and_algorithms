"""
Breadth first traverse

        4
       /  \
      2     8
     / \   / \
    1   3 5  10

    4->2->8->1->3->5->10
"""

from __future__ import annotations
from dataclasses import dataclass
from collections import deque


@dataclass
class Node:
    value: int
    left: Node = None
    right: Node = None


@dataclass
class Tree:
    root: Node = None

    def breadth_first(self):
        queue = deque([self.root])

        while queue:
            current = queue.pop()
            if current.left:
                queue.appendleft(current.left)
            if current.right:
                queue.appendleft(current.right)
            print(current.value, end="->")


if __name__ == "__main__":
    node_1 = Node(1)
    node_3 = Node(3)
    node_5 = Node(5)
    node_10 = Node(10)
    node_2 = Node(2, node_1, node_3)
    node_8 = Node(8, node_5, node_10)
    node_4 = Node(4, node_2, node_8)

    tree = Tree(node_4)
    tree.breadth_first()
