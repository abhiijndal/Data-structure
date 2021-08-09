


class Node:

    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None

    def insert(self,data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left=Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right=Node(data)
                else:
                    self.right.insert(data)
            #else:
                #self.data=data
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)

        if self.right:
            self.right.print_tree()
        
root=Node(100)
root.insert(78)
root.insert(90)
root.insert(0)
root.insert(67)
root.insert(465)
root.insert(787)
root.insert(909)
root.print_tree()                

