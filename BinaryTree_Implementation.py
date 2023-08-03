class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        newNode = Node(value)

        if self.root is None:
            self.root = newNode
            return self
        
        currentNode = self.root
        while True:
            if newNode.value < currentNode.value:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return self
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return self
                currentNode = currentNode.right
            
    def lookup(self, value):
        pass
    
    def remove(self, value):
        pass
    
    def print_tree(self):
        def print_inorder(node):
            if node is not None:
                print_inorder(node.left)
                print(node.value, end=" ")
                print_inorder(node.right)

        print_inorder(self.root)
        print()
    
myTree = BinarySearchTree()

myTree.insert(9)
myTree.insert(4)
myTree.insert(20)
myTree.insert(15)
myTree.insert(170)
myTree.insert(1)        
myTree.insert(6)

myTree.print_tree()

