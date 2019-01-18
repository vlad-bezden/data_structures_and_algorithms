"""
In-order traversal of binary tree

              A
             / \
            B   C
           / \   \
          D   E   F
         / \
        G   H

    G->D->H->B->E->A->F->C
"""


from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    data: str
    left: Node = None
    right: Node = None


@dataclass
class Tree:
    root: Node

    def in_order(self, node: Node) -> None:
        if not node:
            return
        self.in_order(node.left)
        print(node.data, end="->")
        self.in_order(node.right)


if __name__ == "__main__":
    h = Node("H")
    g = Node("G")
    f = Node("F")
    e = Node("E")
    d = Node("D", g, h)
    c = Node("C", f)
    b = Node("B", d, e)
    a = Node("A", b, c)

    tree = Tree(a)
    tree.in_order(a)
