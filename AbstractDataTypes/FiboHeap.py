from math import floor, log


class FibonacciHeapNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.child = None
        self.left = self
        self.right = self
        self.degree = 0
        self.mark = False

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return str(self.key)


class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.n = 0

    def insert(self, x):
        x = FibonacciHeapNode(x)
        if self.min is not None:
            x.left = self.min
            x.right = self.min.right
            self.min.right = x
            x.right.left = x
            if x.key < self.min.key:
                self.min = x
        else:
            self.min = x
        self.n += 1

    def extract_min(self):
        z = self.min
        if z is not None:
            for x in z.children:
                x.parent = None
                x.left = self.min
                x.right = self.min.right
                self.min.right = x
                x.right.left = x
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return z

    def consolidate(self):
        A = [None] * (floor(log(self.n, 2)) + 1)
        w = self.min
        for _ in range(self.n):
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.link(y, x)
                A[d] = None
                d += 1
            A[d] = x
            w = w.right
        self.min = None
        for k in A:
            if k is not None:
                k.left = k
                k.right = k
                if self.min is not None:
                    k.left = self.min
                    k.right = self.min.right
                    self.min.right = k
                    k.right.left = k
                    if k.key < self.min.key:
                        self.min = k
                else:
                    self.min = k

    def link(self, y, x):
        y.left.right = y.right
        y.right.left = y.left
        if x.right == x:
            self.min = x
        y.left = x
        y.right = x.right
        x.right = y
        y.right.left = y
        y.parent = x
        if x.child is None:
            x.child = y
        x.degree += 1
        y.mark = False
