class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        position = 0
        if self.head:
            position += 1
            current_node = self.head
            while current_node.head:
                current_node = current_node.head
                position += 1
            new_node.key = position
            current_node.head = new_node
        else:
            new_node.key = position
            self.head = new_node

    def add_double(self, data):
        new_node = Node(data)
        position = 0
        if self.head:
            current_node = self.head
            while current_node.head:
                current_node = current_node.head
                position += 1
            new_node.key = position
            new_node.rear, current_node.head = current_node, new_node
        else:
            new_node.key = position
            self.head = new_node

    def get(self, key):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                return current_node.data
            current_node = current_node.head
        return None

    def get_node(self, key):
        current_node = self.head
        while current_node:
            if current_node.key == key:
                return current_node
            current_node = current_node.head
        return None

    def find_key(self, query):
        current_node = self.head
        while current_node:
            if current_node.data == query:
                return current_node.key
            current_node = current_node.head
        return None

    def find_node(self, query):
        current_node = self.head
        while current_node:
            if current_node.data == query:
                return current_node
            current_node = current_node.head
        return None

    def remove(self, key):
        removal = self.get_node(key)
        prior = self.get_node(key - 1)
        post = self.get_node(key + 1)

        if removal:
            lost_data = removal.data
            if prior and post:
                prior.head = post
                if post.rear:
                    post.rear = prior
                self.update_keys(post, key)
            elif prior:
                prior.head = post
            elif post:
                if post.rear:
                    post.rear = None
                self.head = post
                self.update_keys(post, key)
            else:
                self.head = None
            removal = None
        return lost_data

    def remove_by_value(self, value):
        removal = self.find_node(value)
        prior = self.get_node(removal.key - 1)
        post = self.get_node(removal.key + 1)

        if removal:
            lost_data = removal.data
            if prior and post:
                prior.head = post
                if post.rear:
                    post.rear = prior
                self.update_keys(post, removal.key)
            elif prior:
                prior.head = post
            elif post:
                if post.rear:
                    post.rear = None
                self.head = post
                self.update_keys(post, removal.key)
            else:
                self.head = None
            removal = None
        return lost_data

    def insert(self, key, data, doubleLink=False):
        post = self.get_node(key)
        prior = self.get_node(key - 1)
        if doubleLink:
            new_node = Node(data, key, post, prior)
        else:
            new_node = Node(data, key, post)
        if prior is None:
            self.head = new_node
        else:
            prior.head = new_node
        if post:
            self.update_keys(post, key + 1)

    def update_keys(self, start_from, start_key):
        current_node = start_from
        while current_node:
            current_node.key = start_key
            current_node = current_node.head
            start_key += 1

    def __str__(self):
        current_node = self.head
        strLL = ""
        while current_node.head:
            strLL = strLL + str(current_node.data) + " --  > "
            current_node = current_node.head
        return strLL + str(current_node.data)


class Node:
    def __init__(self, data=None, key=None, head=None, rear=None):
        self.data = data
        self.key = key
        self.head = head
        self.rear = rear
