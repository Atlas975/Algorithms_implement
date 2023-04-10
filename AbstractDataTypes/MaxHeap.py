from ast import Raise


class MaxHeap:
    def __init__(self, data):
        self.heap = data
        n = len(self.heap)
        for i in range(n // 2, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        m = i
        l = i * 2 + 1
        r = i * 2 + 2
        n = len(self.heap)

        if l < n and (self.heap[m] < self.heap[l]):
            m = l
        if r < n and (self.heap[m] < self.heap[r]):
            m = r
        if m != i:
            self.heap[i], self.heap[m] = self.heap[m], self.heap[i]
            self.heapify(m)

    def heappush(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1
        par = (i - 1) // 2

        while i != 0 and (self.heap[par] < self.heap[i]):
            self.heap[par], self.heap[i] = self.heap[i], self.heap[par]
            i = par
            par = (i - 1) // 2

    def heappop(self):
        if not self.heap:
            Raise(ValueError("Heap is empty"))
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]

        val = self.heap.pop()
        self.heapify(0)
        return val


if __name__ == "__main__":
    import random

    data = random.sample(range(100), 10)
    print(f"Dataset: {data}\n")
    minheap = MaxHeap(data)
    print(minheap.heap)
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")
    print(f"Popped value: {minheap.heappop()}")

    minheap.heappush(999)
    print(minheap.heap)
    val = minheap.heappop()
    print(f"Popped value: {val}")
