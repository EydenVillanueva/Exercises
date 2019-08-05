class Node:
    def __init__(self,data):
        self.left = None
        self.rigth = None
        self.data = data

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.rigth is None:
                    self.rigth = Node(data)
                else:
                    self.rigth.insert(data)
        else:
            self.data = data

class BinaryTree:
    def __init__(self,node):
        self.node = node



