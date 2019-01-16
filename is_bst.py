"""Checks if Binary Search Tree (BST) is balanced"""

from __future__ import annotations
import sys
from dataclasses import dataclass

MAX_VALUE = sys.maxsize
MIN_VALUE = -sys.maxsize - 1


@dataclass
class Node:
    value: int
    left: Node
    right: Node

    @property
    def is_leaf(self):
        return not self.left and not self.right


def is_bst(node: Node, min_value: int, max_value: int) -> bool:
    if node.value < min_value or max_value < node.value:
        return False
    elif node.is_leaf:
        return True

    return is_bst(node.left, min_value, node.value) and is_bst(
        node.right, node.value, max_value
    )


if __name__ == "__main__":
    node5 = Node(5, None, None)
    node25 = Node(25, None, None)
    node40 = Node(40, None, None)
    node10 = Node(10, None, None)

    # balanced tree
    node30 = Node(30, node25, node40)
    root = Node(20, node10, node30)
    print(is_bst(root, MIN_VALUE, MAX_VALUE))

    # unbalanced tree
    node30 = Node(30, node5, node40)
    root = Node(20, node10, node30)
    print(is_bst(root, MIN_VALUE, MAX_VALUE))
