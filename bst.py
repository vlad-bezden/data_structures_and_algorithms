"""
Basic example of BST
"""

from __future__ import annotations
from dataclasses import dataclass
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


if __name__ == "__main__":
    MAX_VAL = 10 ** 3
    NODES = 100
    root_value = random.randint(0, MAX_VAL)
    tree = Tree(Node(root_value))
    for i in random.sample(range(MAX_VAL), NODES):
        tree.insert(i)

    print(f"Root value: {tree.root.value}")
    print(f"min tree value {tree.min.value}")
    print(f"max tree value {tree.max.value}")
