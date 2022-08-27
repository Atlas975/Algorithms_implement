from LinkedList import LinkedList

class Queue:
    def __init__(self):
        self.data = LinkedList()

    def is_empty(self):
        return self.data.head==None

    def enqueue(self,element):
        self.data.add(element)

    def dequeue(self):
        return self.data.remove(0)

    def peek(self):
        return self.data.get(0)


