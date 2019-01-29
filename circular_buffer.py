"""
Example of circular buffer using regular list
"""


class CircularBuffer:
    def __init__(self, size):
        self.buffer = [None] * size
        self.size = size
        self.count = 0
        self.tail = 0
        self.head = 0

    @property
    def is_empty(self):
        return self.count == 0

    @property
    def is_full(self):
        return self.count == self.size

    def __len__(self):
        return self.count

    def add(self, value):
        # if buffer is full overwrite the value
        if self.is_full:
            self.tail = (self.tail + 1) % self.size
        else:
            self.count += 1
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.size

    def remove(self):
        if self.count == 0:
            raise Exception("Circular Buffer is empty")
        value = self.buffer[self.tail]
        self.tail = (self.tail + 1) % self.size
        self.count -= 1
        return value

    def __iter__(self):
        index = self.tail
        counter = self.count
        while counter > 0:
            yield self.buffer[index]
            index = (index + 1) % self.size
            counter -= 1

    def __repr__(self):
        return "[]" if self.is_empty else "[" + ",".join(str(i) for i in self) + "]"
