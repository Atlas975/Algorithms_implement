from LinkedList import LinkedList

class Stack:
    def __init__(self):
        self.data = LinkedList()

    def is_empty(self):
        return self.data.head==None

    def push(self,element):
        self.data.insert(0,element)

    def pop(self):
        return self.data.remove(0)

    def peek(self):
        return self.data.get(0)
