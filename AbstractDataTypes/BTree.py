from typing import Optional

class BNode:
    def __init__(self, keys=None, children=None):
        self.keys = keys or []
        self.children = children or []

    def is_full(self, t):
        return len(self.keys) == (2 * t) - 1

class BTree:
    def __init__(self, t):
        self.root = BNode()
        self.t = t

    def search(self, k) -> Optional[tuple[BNode, int]]:
        node = self.root
        while node:
            i = 0
            while i < len(node.keys) and k > node.keys[i]:
                i += 1
            if i < len(node.keys) and k == node.keys[i]:
                return (node, i)
            elif node.is_leaf():
                return None
            node = node.children[i]
        return None

    def insert(self, k):
        r = self.root
        if r.is_full(self.t):
            s = BNode(children=[r])
            self.root = s
            self._split_child(s, 0)
            self._insert_non_full(s, k)
        else:
            self._insert_non_full(r, k)

    def _insert_non_full(self, node, k):
        i = len(node.keys) - 1
        if node.is_leaf():
            node.keys.append(0)
            while i >= 0 and k < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = k
        else:
            while i >= 0 and k < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == (2 * self.t) - 1:
                self._split_child(node, i)
                if k > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], k)

    def _split_child(self, node, i):
        t = self.t
        y = node.children[i]
        z = BNode(keys=y.keys[t:], children=y.children[t:])
        y.keys = y.keys[:t-1]
        y.children = y.children[:t]
        node.children.insert(i+1, z)
        node.keys.insert(i, y.keys[-1])

    def __str__(self):
        return self._to_string(self.root, "")

    def _to_string(self, node, prefix):
        s = prefix + str(node.keys) + "\n"
        for i, child in enumerate(node.children):
            s += self._to_string(child, prefix + " "*(i!=len(node.children)-1) + "| ")
        return s



def main():
    t = BTree(2)
    for i in range(1, 5):
        t.insert(i)
    print(t)
    print(t.search(2))

if __name__ == "__main__":
    main()