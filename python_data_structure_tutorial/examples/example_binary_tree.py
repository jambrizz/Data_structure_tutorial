"""
In this example problem, we will be using binary trees to add, remove, check for membership, size of set.
You can copy and paste the code below to test out the code in your own environment.
"""

# Create a class for a node
class BinarySearchTree:
    
    # Create a method to initialize the node
    def Node(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    # Initialize an empty tree    
    def __init__(self):
        self.root = None
        
    # Create a method to add a node to the tree we created
    def addNode(self, data):
        if self.root == None:
            self.root = self.Node(data)
        else:
            self.add_node(data, self.root)
            
    # Create a method to delete a node from the tree we created
    def removeNode(self, key):
        if self.root is not None:
            self.root = self.remove_Node(key, self.root)
            
    # Create a method to find a node in the tree we created
    def findNode(self, key):
        if self.root is not None:
            return self.find_Node(key, self.root)
        else:
            return None
        
    # Create a method to print the tree we created
    def printTree(self):
        if self.root is not None:
            self.print_Tree(self.root)
            
    # create a method to traverse the tree forward
    def traverseForward(self):
        if self.root is not None:
            self.traverse_forward(self.root)
            
    # create a method to traverse the tree backward
    def traverseBackward(self):
        if self.root is not None:
            self.traverse_backward(self.root)
            
    # Create a method to find the size of the tree we created
    def treeHeight(self):
        if self.root is not None:
            return self.tree_height(self.root, 0)
        else:
            return 0
        