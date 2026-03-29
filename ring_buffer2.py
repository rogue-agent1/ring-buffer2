#!/usr/bin/env python3
"""Ring buffer (circular buffer) implementation."""

class RingBuffer:
    def __init__(self, capacity: int):
        self._buf = [None] * capacity
        self._capacity = capacity
        self._head = 0  # next write position
        self._size = 0

    def push(self, item):
        self._buf[self._head] = item
        self._head = (self._head + 1) % self._capacity
        if self._size < self._capacity:
            self._size += 1

    def pop(self):
        if self._size == 0:
            raise IndexError("pop from empty buffer")
        tail = (self._head - self._size) % self._capacity
        item = self._buf[tail]
        self._size -= 1
        return item

    def peek(self):
        if self._size == 0:
            raise IndexError("peek at empty buffer")
        tail = (self._head - self._size) % self._capacity
        return self._buf[tail]

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._size > 0

    @property
    def full(self):
        return self._size == self._capacity

    def to_list(self):
        result = []
        for i in range(self._size):
            idx = (self._head - self._size + i) % self._capacity
            result.append(self._buf[idx])
        return result

    def clear(self):
        self._head = 0
        self._size = 0

if __name__ == "__main__":
    rb = RingBuffer(5)
    for i in range(8):
        rb.push(i)
    print(f"Contents: {rb.to_list()}")
    print(f"Size: {len(rb)}, Full: {rb.full}")

def test():
    rb = RingBuffer(3)
    assert len(rb) == 0
    rb.push(1); rb.push(2); rb.push(3)
    assert len(rb) == 3
    assert rb.full
    assert rb.to_list() == [1, 2, 3]
    # Overflow
    rb.push(4)
    assert rb.to_list() == [2, 3, 4]
    assert len(rb) == 3
    # Pop (FIFO)
    assert rb.pop() == 2
    assert rb.pop() == 3
    assert len(rb) == 1
    # Peek
    assert rb.peek() == 4
    # Clear
    rb.clear()
    assert len(rb) == 0
    assert not rb
    # Error on empty
    try:
        rb.pop()
        assert False
    except IndexError:
        pass
    print("  ring_buffer2: ALL TESTS PASSED")
