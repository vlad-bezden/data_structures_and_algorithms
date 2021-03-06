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

    def find(self, value: int) -> Node:
        """Finds node by value."""
        current = self.root
        while current:
            if current.value == value:
                return current
            current = current.left if value < current.value else current.right
        return current

    def in_order(self, node: Node) -> Node:
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

    def __iter__(self) -> Tree:
        self.current = self.in_order(self.root)
        return self

    def __next__(self) -> Node:
        return next(self.current)

    def __repr__(self) -> str:
        """In-order tree print"""
        trace = []
        for n in self.in_order(self.root):
            trace.append(n.value)

        return "->".join(map(str, trace))


if __name__ == "__main__":
    MAX_VAL = 10 ** 3
    NODES = 20
    random.seed(42)
    root_value = random.randint(0, MAX_VAL)
    tree = Tree(Node(root_value))
    for i in random.sample(range(MAX_VAL), NODES):
        tree.insert(i)

    print(f"Root value: {tree.root.value}")
    print(f"min tree value {tree.min.value}")
    print(f"max tree value {tree.max.value}")

    print(tree)

    for node in tree:
        print(node.value)

    # this value is not part of the tree
    node = tree.find(256)
    assert node is None
    node = tree.find(250)
    assert node.value == 250

    print("DONE")
