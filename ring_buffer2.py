#!/usr/bin/env python3
"""Lock-Free Ring Buffer — SPSC (single producer, single consumer)."""

class RingBuffer:
    def __init__(self, capacity):
        self.cap = capacity; self.buf = [None] * capacity
        self.head = 0; self.tail = 0
    def push(self, item):
        next_head = (self.head + 1) % self.cap
        if next_head == self.tail: return False
        self.buf[self.head] = item; self.head = next_head; return True
    def pop(self):
        if self.tail == self.head: return None
        item = self.buf[self.tail]; self.tail = (self.tail + 1) % self.cap; return item
    def __len__(self): return (self.head - self.tail) % self.cap
    def is_empty(self): return self.head == self.tail
    def is_full(self): return (self.head + 1) % self.cap == self.tail
    def peek(self): return self.buf[self.tail] if not self.is_empty() else None

if __name__ == "__main__":
    rb = RingBuffer(8)
    for i in range(6): rb.push(i)
    print(f"Len: {len(rb)}, Pop: {[rb.pop() for _ in range(3)]}, Len after: {len(rb)}")
    print(f"Peek: {rb.peek()}, Full: {rb.is_full()}")
