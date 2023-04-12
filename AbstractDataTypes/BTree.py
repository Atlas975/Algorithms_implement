class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.values = []
        self.leaf = leaf
        self.children = []

    def add_key_value(self, key, value):
        self.keys.append(key)
        self.values.append(value)

    def split(self, parent, index):
        new_node = BTreeNode(self.leaf)
        mid = len(self.keys) // 2
        median_key = self.keys[mid]
        median_value = self.values[mid]

        new_node.keys = self.keys[mid + 1 :]
        new_node.values = self.values[mid + 1 :]
        self.keys = self.keys[:mid]
        self.values = self.values[:mid]

        if not self.leaf:
            new_node.children = self.children[mid + 1 :]
            self.children = self.children[: mid + 1]

        parent.add_key_value(median_key, median_value)
        parent.add_child(new_node, index)

    def add_child(self, node, index):
        self.children.insert(index + 1, node)

    def get_node_index(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return i
        return len(self.keys)

    def is_full(self, t=2):
        return len(self.keys) == 2 * t - 1

    def search(self, key):
        i = 0
        while i < len(self.keys) and key > self.keys[i]:
            i += 1
        if i < len(self.keys) and key == self.keys[i]:
            return self.values[i]
        elif self.leaf:
            return None
        else:
            return self.children[i].search(key)


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def search(self, key):
        return self.root.search(key)

    def insert(self, key, value):
        node = self.root
        if node.is_full():
            new_root = BTreeNode(False)
            new_root.children.append(self.root)
            self.root = new_root
            node = self.root
            node.split(new_root, 0)
        while not node.leaf:
            index = node.get_node_index(key)
            if node.children[index].is_full():
                node.children[index].split(node, index)
                if key > node.keys[index]:
                    index += 1
            node = node.children[index]

        node.add_key_value(key, value)

    def __str__(self):
        nodes = [self.root]
        result = ""
        while nodes:
            new_nodes = []
            line = ""
            for node in nodes:
                if node.leaf:
                    line += " ".join([f"{k}:{v}" for k, v in zip(node.keys, node.values)])
                else:
                    line += " ".join([str(k) for k in node.keys])
                    new_nodes += node.children
                line += " | "
            result += line + "\n"
            nodes = new_nodes
        return result


def main():
    t = BTree(2)
    for i in range(1, 5):
        t.insert(i, i * 10)
    print(t)
    print(t.search(2))


if __name__ == "__main__":
    main()
