
# lets create a binary tree under 100 days coding challenge
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.value = value

    def printTree(self):
        leftStr = "NULL"
        rightStr = "NULL"
        if self.left is not None:
            leftStr = "[ " + self.left.printTree() + " ]"

        if self.right is not None:
            rightStr = "[ " + self.right.printTree() + " ]"

        string =   leftStr + " <- " + str(self.value) + " -> " + rightStr 
        return string 

    def insert(self,value):
        if value <= self.value:
            if self.left == None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right == None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    


# lets create a simple binary tree
# root node
root = Node(1)

# right now the tree looks like this

#    0
#   / \
#  /   \
# None None

# First version of the code
#root.left = Node(1)
#root.right = Node(2)
#root.left.left= Node(3)

root.insert(0)
root.insert(2)
root.insert(3)
root.insert(1)

print(root.printTree())