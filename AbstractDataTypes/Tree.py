
class TreeNode:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
    def add(self,insert):
        pass


    def __str__(self):
        padding=" \t "
        print(f"  {self.data}")
        print(f"|{padding}|")
        print(f"{self.left.data}{padding}{self.right.data}")








