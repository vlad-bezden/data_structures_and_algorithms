"""
Heap (min-heap) implementation example
"""

from random import sample


HEAP_SIZE = 20


class EmptyHeapError(Exception):
    def __init__(self):
        super().__init__("No elements in the heap")


class Heap:
    def __init__(self):
        self.__heap = [0]

    @property
    def size(self) -> int:
        return len(self.__heap) - 1

    def __len__(self) -> int:
        return self.size

    @property
    def is_empty(self) -> bool:
        return self.size <= 0

    def insert(self, item: int) -> None:
        self.__heap.append(item)
        self.arrange(self.size)

    def __iter__(self):
        self.__current = 0
        return self

    def __next__(self):
        self.__current += 1
        if not self.is_empty:
            return self.__heap[self.__current]
        else:
            raise StopIteration

    def arrange(self, index: int) -> None:
        """Rebalances tree"""
        parent_index = index // 2
        if parent_index <= 0:
            return
        if self.__heap[index] < self.__heap[parent_index]:
            self.__heap[index], self.__heap[parent_index] = (
                self.__heap[parent_index],
                self.__heap[index],
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
        return l_index if self.__heap[l_index] < self.__heap[r_index] else r_index

    def sink(self, index: int) -> None:
        """Rebalances the tree when item is popped"""
        child_index = self._child_min_index(index)
        if self.size < child_index:
            return
        if self.__heap[child_index] < self.__heap[index]:
            self.__heap[index], self.__heap[child_index] = (
                self.__heap[child_index],
                self.__heap[index],
            )
        self.sink(child_index)

    def pop(self) -> int:
        """Pop root (lowest element) of the tree"""
        if self.is_empty:
            raise EmptyHeapError()
        item = self.__heap[1]
        # get latest element in the heap and put it to the root of the tree
        last_item = self.__heap.pop()
        if not self.is_empty:
            self.__heap[1] = last_item
            # rebalance a tree
            self.sink(1)
        return item

    def clear(self):
        self.__heap = [0]

    def __repr__(self):
        return str(self.__heap[1:])


def main():
    heap = Heap()
    assert heap.size == len(heap) == 0
    assert heap.is_empty is True

    items = [i for i in sample(range(100), HEAP_SIZE)]
    for item in items:
        heap.insert(item)

    assert heap.size == len(heap) == HEAP_SIZE
    print(f"items: {items}")
    print(f"heap: {heap}")

    heap.clear()
    assert heap.is_empty is True
    assert heap.size == 0

    items = [4, 8, 7, 2, 9, 10, 5, 1, 3, 6]
    for item in items:
        heap.insert(item)
        print(f"item: {item}, heap: {heap}")

    while not heap.is_empty:
        item = heap.pop()
        print(f"item: {item}, heap: {heap}")

    try:
        heap.pop()
        assert False, "Failed. There are no elements in the heap"
    except EmptyHeapError as ex:
        print(f"Exeption: {ex}")


if __name__ == "__main__":
    main()
