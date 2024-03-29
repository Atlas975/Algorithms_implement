import random


from queue import PriorityQueue

def a_star():
    pass


class State(object):
    def __init__(self,value,parent,start=0,goal=0,solver=0):
        self.children = []
        self.parent = parent
        self.value = value
        self.distance = 0
        if parent:
            self.path = parent.path[:]
            self.path.append(value)
            self.start = parent.start
            self.goal = parent.goal
        else:
            self.path = [value]
            self.start = start
            self.goal = goal

class State_string(State):
    def __init__(self,value,parent,start=0,goal=0):
        super(State_string,self).__init__(value,parent,start,goal)
        self.dist=self.get_dist()

    def get_dist(self):
        if self.goal == self.value:
            return 0
        dist=0
        for i in range(len(self.value)):
            letter=self.goal[i]
            dist+=abs(i-self.value.index(letter))
        return dist

    def create_children(self):
        if not self.children:
            for i in range(len(self.goal)-1):
                val=self.value
                val=val[:i]+val[i+1]+val[i]+val[child=State_string(val,self)]


if __name__ == '__main__':
    data = random.sample(range(1000),10)
    print(f"Dataset: {data}")
    sorted_data=a_star(data)
    print(f"Sorted dataset: {sorted_data}")

