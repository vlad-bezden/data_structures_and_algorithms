"""
in-order, pre-order and post-order traversal of binary tree

              A
             / \
            B   C
           / \   \
          D   E   F
         / \
        G   H

    in-order
    G->D->H->B->E->A->F->C
    pre-order
    A->B->D->G->H->E->C->F
    post-order
    G->H->D->E->B->F->C->A
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

    def pre_order(self, node: Node) -> None:
        if not node:
            return
        print(node.data, end="->")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def post_order(self, node: Node) -> None:
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data, end="->")


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
    print("\nin-order")
    tree.in_order(a)
    print("\npre-order")
    tree.pre_order(a)
    print("\npost-order")
    tree.post_order(a)
