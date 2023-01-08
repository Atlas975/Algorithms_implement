from ast import Raise
from dataclasses import dataclass, field
from typing import List, Union

NUM = Union[int, float]
VECTOR = List[NUM]


@dataclass
class Maxheap:
    heap: VECTOR = field(default_factory=list)

    def __post_init__(self) -> None:
        self.size = len(self.heap)
        for i in range(self.size // 2, -1, -1):
            self.heapify(i)

    def heapify(self, idx: int = 0) -> None:
        root = idx
        left = idx * 2 + 1
        right = idx * 2 + 2
        if (left < self.size) and (self.heap[root] < self.heap[left]):
            root = left
        if (right < self.size) and (self.heap[root] < self.heap[right]):
            root = right
        if root != idx:
            self.heap[idx], self.heap[root] = self.heap[root], self.heap[idx]
            self.heapify(root)

    def heappush(self, val: NUM) -> None:
        self.heap.append(val)
        self.size += 1
        idx = self.size - 1
        parent = idx // 2
        while self.heap[idx] > self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx, parent = parent, parent // 2

    def heappop(self) -> NUM:
        if self.size == 0:
            Raise(ValueError("Heap is empty"))
        self.size -= 1
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        val = self.heap.pop(-1)
        self.heapify()
        return val





if __name__ == "__main__":
    import random

    data: VECTOR = random.sample(range(100), 10)
    print(f"Dataset: {data}\n")
    minheap = Maxheap(data)
    print(minheap)
    val = minheap.heappop()
    print(f"Popped value: {val}")
    val = minheap.heappop()
    print(f"Popped value: {val}")
    minheap.heappush(100)
    print(minheap)
    val = minheap.heappop()
    print(f"Popped value: {val}")
