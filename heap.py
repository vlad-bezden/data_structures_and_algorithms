"""
Heap (min-heap) implementation example
"""

import sys
from dataclasses import dataclass
from random import sample


HEAP_SIZE = 20


@dataclass
class Heap:
    heap = [0]

    @property
    def size(self) -> int:
        return len(self.heap) - 1

    @property
    def is_empty(self) -> bool:
        return self.size <= 0

    def insert(self, item: int) -> None:
        self.heap.append(item)
        self.arrange(self.size)

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        self.__current += 1
        if self.__current < self.size:
            return self.heap[self.__current]
        else:
            raise StopIteration

    def arrange(self, index: int) -> None:
        """Rebalances tree"""
        parent_index = index // 2
        if parent_index <= 0:
            return
        if self.heap[index] < self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = (
                self.heap[parent_index],
                self.heap[index],
            )
        self.arrange(parent_index)

    def _child_min_index(self, index: int) -> int:
        """Finds child min index that has min value

        For instance two children 10, 6 with indexes 3, 4
        will return index 4
        """
        l_index = index * 2
        r_index = l_index + 1
        if self.size < r_index:
            return l_index
        return l_index if self.heap[l_index] < self.heap[r_index] else r_index

    def sink(self, index: int) -> None:
        """Rebalances the tree when item is popped"""
        child_index = self._child_min_index(index)
        if self.size < child_index:
            return
        if self.heap[child_index] < self.heap[index]:
            self.heap[index], self.heap[child_index] = (
                self.heap[child_index],
                self.heap[index],
            )
        self.sink(child_index)

    def pop(self) -> int:
        """Pop root (lowest element) of the tree"""
        if self.is_empty:
            return None
        item = self.heap[1]
        # get latest element in the heap and put it to the root of the tree
        last_item = self.heap.pop()
        if not self.is_empty:
            self.heap[1] = last_item
            # rebalance a tree
            self.sink(1)
        return item

    def __repr__(self):
        return f"[{', '.join(map(str, self.heap[1:]))}]"


def main():
    heap = Heap()
    assert heap.size == 0
    assert heap.is_empty is True

    items = [i for i in sample(range(100), HEAP_SIZE)]
    for item in items:
        heap.insert(item)

    assert heap.size == HEAP_SIZE
    print(f"items: {items}")
    print(f"heap: {heap}")

    while not heap.is_empty:
        item = heap.pop()
        print(f"item: {item}, heap: {heap}")


if __name__ == "__main__":
    main()
