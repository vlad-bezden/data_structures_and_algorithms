"""
BST Tree implementation example

           --50--
         /        \
        /          \
      25            75
     /  \         /    \
   10     33    56      89
  /  \   / \   /  \    /  \
 4   11 30 40 52  61  82  95
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Node:
    value: int
    left: Optional[Node] = None
    right: Optional[Node] = None

    @property
    def is_leaf(self):
        return not (self.left or self.right)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return self.value == other.value

    def __ne__(self, other) -> bool:
        if not isinstance(other, Node):
            return NotImplemented
        return not self.__eq__(other)

    def __lt__(self, other: Node) -> int:
        return self.value < other.value

    def __gt__(self, other: Node) -> int:
        return not self.__lt__(other)

    def __repr__(self):
        return str(self.value)


class BST:
    def __init__(self, value: int) -> None:
        self.root = Node(value)

    def _in_order(self, parent: Optional[Node]) -> None:
        if parent:
            self._in_order(parent.left)
            print(parent, end="->")
            self._in_order(parent.right)

    def in_order(self):
        self._in_order(self.root)

    def _height(self, parent: Optional[Node]) -> int:
        if parent is None or parent.is_leaf:
            return 0
        return 1 + max(self._height(parent.left), self._height(parent.right))

    def _search(self, value: int, node: Optional[Node]) -> Optional[Node]:
        if node:
            if node.value == value:
                return node
            elif node.value < value:
                return self._search(value, node.right)
            else:
                return self._search(value, node.left)
        return None

    def search(self, value: int) -> Optional[Node]:
        return self._search(value, self.root)

    def add(self, value: int) -> Node:
        node = Node(value)
        current = self.root
        while current:
            if node < current:
                if current.left is None:
                    current.left = node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = node
                    break
                else:
                    current = current.right
        return node

    def _leaf_count(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        elif node.is_leaf:
            return 1
        return self._leaf_count(node.left) + self._leaf_count(node.right)

    @property
    def leaf_count(self) -> int:
        """Counts number of leafs in the tree"""
        return self._leaf_count(self.root)

    @property
    def height(self) -> int:
        return self._height(self.root)

    def _size(self, node: Optional[Node]) -> int:
        if node is None:
            return 0
        else:
            return 1 + self._size(node.left) + self._size(node.right)

    @property
    def size(self):
        return self._size(self.root)


def main():
    tree = BST(50)
    tree.add(25)
    tree.add(75)
    tree.add(10)
    tree.add(4)
    tree.add(11)
    tree.add(33)
    tree.add(89)
    tree.add(40)
    tree.add(30)
    tree.add(56)
    tree.add(61)
    tree.add(52)
    tree.add(82)
    tree.add(95)
    result = tree.height
    print(f"Tree height is: {result}")
    assert result == 3
    result = tree.leaf_count
    assert result == 8
    print(f"There are {result} leafs in the tree")
    result = tree.size
    print(f"There are {result} nodes in the tree")
    assert result == 15
    tree.in_order()
    result = tree.search(95)
    assert result.value == 95
    result = tree.search(100)
    assert result is None


if __name__ == "__main__":
    main()
    print("DONE!!!")
