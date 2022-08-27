from ast import Raise
from dataclasses import dataclass, field
from typing import List, Union

NUM = Union[int, float]
VECTOR = List[NUM]

@dataclass
class Maxheap:
    heap: VECTOR = field(default_factory=list)

    def __init__(self, args: VECTOR) :
        self.heap = args
        self.size=len(self.heap)
        for i in range(len(self.heap)//2, -1, -1):
            self.heapify(i)

    def get_parent_idx(self, idx: int) -> int:
        idx //= 2
        return -1 if idx < 0 else idx

    def get_left_idx(self,idx:int) -> int:
        idx = idx*2+1
        return -1 if idx >= self.size else idx

    def get_right_idx(self,idx:int ) -> int:
        idx=idx*2+2
        return -1 if idx>= self.size else idx

    def swap(self, node1:int , node2:int) -> None:
        self.heap[node1], self.heap[node2] = self.heap[node2], self.heap[node1]

    def is_leaf(self,idx) -> bool:
        return idx*2 > len(self.heap)

    def heapify(self, idx: int = 0) -> None:
        largest = idx
        left = self.get_left_idx(idx)
        right = self.get_right_idx(idx)
        if left != -1 and self.heap[largest] < self.heap[left]:
            largest = left
        if right != -1 and self.heap[largest] < self.heap[right]:
            largest = right
        if largest != idx:
            self.swap(idx, largest)
            self.heapify(largest)

    def heappush(self,val: NUM) -> None:
        self.heap.append(val)
        self.size += 1
        curr=self.size-1
        while self.heap[curr] > self.heap[self.get_parent_idx(curr)]:
            self.swap(curr, self.get_parent_idx(curr))
            curr=self.get_parent_idx(curr)


    def heapop(self) -> NUM:
        if self.size == 0: Raise(ValueError("Heap is empty"))
        val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.size -= 1
        self.heap.pop(-1)
        self.heapify()
        return val

if __name__ == '__main__':
    import random
    data: VECTOR = random.sample(range(100),10)
    print(f"Dataset: {data}\n")
    minheap = Maxheap(data)
    print(minheap)
    val=minheap.heapop()
    print(f"Popped value: {val}")
    val=minheap.heapop()
    print(f"Popped value: {val}")
    minheap.heappush(100)
    print(minheap)
    val=minheap.heapop()
    print(f"Popped value: {val}")

