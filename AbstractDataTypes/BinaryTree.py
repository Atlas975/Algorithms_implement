from collections import deque
from dataclasses import dataclass
from typing import Optional

@dataclass
class Node:
    val: int
    left: Optional['Node'] = None
    right: Optional['Node'] = None

@dataclass
class Tree:
    root: Optional[Node] = None

    def add(self,val):
        if self.root is None:
            self.root=Node(val)
            return
        stack=deque([self.root])
        while stack:
            current=stack.pop()
            r=current.right
            l=current.left
            if l is None:
                current.left=Node(val)
                return
            if r is None:
                current.right=Node(val)
                return
            stack.append(r)
            stack.append(l)

    def pop(self,idx):




