"""
Basic example of BST
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import List
import random


@dataclass
class Node:
    value: int
    left: Node = None
    right: Node = None


@dataclass
class Tree:
    root: Node = None

    def insert(self, value: int) -> Node:
        """Inserts new node to the tree."""
        node = Node(value)

        if self.root is None:
            self.root = node
            return
        else:
            current = self.root

        while current:
            if node.value < current.value:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            elif current.value < node.value:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right
        return node

    @property
    def min(self) -> Node:
        """Finds minimum node"""
        current = self.root
        while current.left:
            current = current.left
        return current

    @property
    def max(self) -> Node:
        """Finds node with max value"""
        current = self.root
        while current.right:
            current = current.right
        return current

    def in_order(self, node: Node) -> List[str]:
        """
        Process left sub tree
        Current tree
        Process right sub tree
        """
        if node.left:
            for n in self.in_order(node.left):
                yield n
        yield node
        if node.right:
            for n in self.in_order(node.right):
                yield n

    def __repr__(self):
        """In-order tree print"""
        trace = []
        for n in self.in_order(self.root):
            trace.append(n.value)

        return "->".join(map(str, trace))


if __name__ == "__main__":
    MAX_VAL = 10 ** 3
    NODES = 20
    root_value = random.randint(0, MAX_VAL)
    tree = Tree(Node(root_value))
    for i in random.sample(range(MAX_VAL), NODES):
        tree.insert(i)

    print(f"Root value: {tree.root.value}")
    print(f"min tree value {tree.min.value}")
    print(f"max tree value {tree.max.value}")

    print(tree)
