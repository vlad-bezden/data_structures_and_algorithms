"""Check if Binary Search Tree (BST) is balanced"""

import sys
from collections import namedtuple

MAX_KEY = sys.maxsize
MIN_KEY = -sys.maxsize - 1

Node = namedtuple("Node", ["value", "left", "right"])


def is_root(node: Node) -> bool:
    """Returns True if node has at least one child"""
    return node.left or node.right


def is_bst(root: Node, min_value: int, max_value: int) -> bool:
    if root.value < min_value or max_value < root.value:
        return False
    elif not is_root(root):
        return True

    return is_bst(root.left, min_value, root.value) and is_bst(
        root.right, root.value, max_value
    )


if __name__ == "__main__":
    node5 = Node(5, None, None)
    node25 = Node(25, None, None)
    node40 = Node(40, None, None)
    node10 = Node(10, None, None)

    node30 = Node(30, node25, node40)
    root = Node(20, node10, node30)
    print(is_bst(root, MIN_KEY, MAX_KEY))

    node30 = Node(30, node5, node40)
    root = Node(20, node10, node30)
    print(is_bst(root, MIN_KEY, MAX_KEY))
